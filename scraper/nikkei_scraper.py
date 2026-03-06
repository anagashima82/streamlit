# ============================================================
# nikkei_scraper.py - Yahoo!ファイナンスから日経平均株価を取得
# ============================================================
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import json
import re


def get_mock_data() -> dict:
    """
    スクレイピング失敗時に返すモックデータ
    学習を継続できるようにサンプルデータを提供
    """
    return {
        "success": True,
        "is_mock": True,
        "data": {
            "current_price": "38,500.25",
            "price_change": "+350.75",
            "price_change_percent": "+0.92%",
            "volume": "1,234,567,890",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        },
        "history": [
            {"date": "2024-01-01", "price": 33500},
            {"date": "2024-02-01", "price": 35000},
            {"date": "2024-03-01", "price": 36500},
            {"date": "2024-04-01", "price": 37000},
            {"date": "2024-05-01", "price": 38000},
            {"date": "2024-06-01", "price": 38500},
        ],
        "message": "モックデータを使用しています（Selenium未実行）"
    }


def scrape_nikkei(progress_callback=None) -> dict:
    """
    Yahoo!ファイナンスから日経平均株価データを取得

    Args:
        progress_callback: 進捗を通知するコールバック関数
                          float(0.0〜1.0)とstr(ステータスメッセージ)を受け取る

    Returns:
        dict: 取得したデータを含む辞書
            - success: bool - 取得成功/失敗
            - is_mock: bool - モックデータかどうか
            - data: dict - 株価データ
            - history: list - 履歴データ（グラフ用）
            - message: str - ステータスメッセージ
    """

    # 進捗通知用のヘルパー関数
    def notify_progress(progress: float, message: str):
        if progress_callback:
            progress_callback(progress, message)

    driver = None

    try:
        # ステップ1: ブラウザ起動準備
        notify_progress(0.1, "ブラウザを起動中...")

        # Chrome オプション設定（ヘッドレスモード）
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 画面非表示
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        # WebDriverを起動
        notify_progress(0.2, "ChromeDriverを初期化中...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # ステップ2: ページにアクセス
        notify_progress(0.3, "Yahoo!ファイナンスにアクセス中...")
        url = "https://finance.yahoo.co.jp/quote/998407.O"
        driver.get(url)

        # ステップ3: ページ読み込み待機
        notify_progress(0.5, "ページ読み込み中...")
        time.sleep(2)  # ページ読み込み待機

        # ステップ4: データ取得
        notify_progress(0.7, "データを取得中...")

        # 初期値
        current_price = "取得失敗"
        price_change = "取得失敗"
        price_change_percent = "取得失敗"
        volume = "N/A"

        # 方法1: クラス名で株価を取得（PriceBoard__price）
        try:
            # 株価を取得
            price_element = driver.find_element(
                By.CSS_SELECTOR,
                "span[class*='PriceBoard__price']"
            )
            current_price = price_element.text.strip()

            # 前日比を含む親ブロックを取得
            price_block = driver.find_element(
                By.CSS_SELECTOR,
                "div[class*='PriceBoard__priceBlock']"
            )
            block_text = price_block.text

            # 前日比を正規表現で抽出（例: +165.17 (+0.30%)）
            change_match = re.search(r'([+-]?[0-9,]+\.[0-9]+)\s*\(([+-]?[0-9]+\.[0-9]+%)\)', block_text)
            if change_match:
                price_change = change_match.group(1)
                price_change_percent = change_match.group(2)
        except Exception:
            pass

        # 方法2: 方法1が失敗した場合、StyledNumber クラスで探す
        if current_price == "取得失敗":
            try:
                price_element = driver.find_element(
                    By.CSS_SELECTOR,
                    "span[class*='StyledNumber__value'][class*='PriceBoard']"
                )
                current_price = price_element.text.strip()
            except Exception:
                pass

        # 方法3: 株価らしきspan要素を探す
        if current_price == "取得失敗":
            try:
                spans = driver.find_elements(By.TAG_NAME, "span")
                for span in spans:
                    text = span.text.strip()
                    # 株価のフォーマット（例: 55,438.93）に一致するか
                    if re.match(r'^[0-9]{2},[0-9]{3}\.[0-9]{2}$', text):
                        span_class = span.get_attribute("class") or ""
                        # PriceBoardに関連する要素を優先
                        if "PriceBoard" in span_class or "price" in span_class.lower():
                            current_price = text
                            break
                # PriceBoardが見つからなければ最初の一致を使用
                if current_price == "取得失敗":
                    for span in spans:
                        text = span.text.strip()
                        if re.match(r'^[0-9]{2},[0-9]{3}\.[0-9]{2}$', text):
                            current_price = text
                            break
            except Exception:
                pass

        # 方法4: 前日比が取れていない場合、ページソースから正規表現で抽出
        if price_change == "取得失敗":
            try:
                page_source = driver.page_source
                # changePrice パターンを探す
                change_match = re.search(r'changePrice["\']?\s*[:\=]\s*["\']?([0-9,\.\-\+]+)["\']?', page_source)
                if change_match:
                    change_val = change_match.group(1)
                    if not change_val.startswith("-") and not change_val.startswith("+"):
                        change_val = f"+{change_val}"
                    price_change = change_val

                # changePriceRate パターンを探す
                rate_match = re.search(r'changePriceRate["\']?\s*[:\=]\s*["\']?([0-9,\.\-\+]+)["\']?', page_source)
                if rate_match:
                    rate_val = rate_match.group(1)
                    if not rate_val.startswith("-") and not rate_val.startswith("+"):
                        rate_val = f"+{rate_val}"
                    price_change_percent = f"{rate_val}%"
            except Exception:
                pass

        notify_progress(0.9, "データ整形中...")

        # 取得時刻
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 履歴データ（サンプル）
        history = [
            {"date": "2024-01-01", "price": 33500},
            {"date": "2024-02-01", "price": 35000},
            {"date": "2024-03-01", "price": 36500},
            {"date": "2024-04-01", "price": 37000},
            {"date": "2024-05-01", "price": 38000},
            {"date": "2024-06-01", "price": 38500},
        ]

        notify_progress(1.0, "取得完了！")

        return {
            "success": True,
            "is_mock": False,
            "data": {
                "current_price": current_price,
                "price_change": price_change,
                "price_change_percent": price_change_percent,
                "volume": volume,
                "timestamp": timestamp,
            },
            "history": history,
            "message": "データの取得に成功しました"
        }

    except Exception as e:
        # エラー発生時はモックデータを返す
        notify_progress(1.0, f"エラー発生: {str(e)}")
        mock_data = get_mock_data()
        mock_data["message"] = f"スクレイピングに失敗しました。モックデータを表示します。\nエラー: {str(e)}"
        return mock_data

    finally:
        # ブラウザを閉じる
        if driver:
            driver.quit()


# テスト用
if __name__ == "__main__":
    def print_progress(progress, message):
        print(f"[{progress*100:.0f}%] {message}")

    result = scrape_nikkei(progress_callback=print_progress)
    print("\n結果:")
    print(f"成功: {result['success']}")
    print(f"モック: {result['is_mock']}")
    print(f"データ: {result['data']}")
    print(f"メッセージ: {result['message']}")
