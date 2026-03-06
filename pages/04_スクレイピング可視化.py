# ============================================================
# 04_スクレイピング可視化.py - Seleniumでスクレイピングしてデータを可視化
# ============================================================
import streamlit as st
import pandas as pd
import plotly.express as px
import sys
from pathlib import Path

# scraperモジュールをインポートできるようにパスを追加
sys.path.append(str(Path(__file__).parent.parent))
from scraper.nikkei_scraper import scrape_nikkei, get_mock_data

# ページ設定
st.set_page_config(page_title="スクレイピング可視化", page_icon="📈", layout="wide")

# ============================================================
# session_stateの初期化
# ============================================================
if "scraping_result" not in st.session_state:
    st.session_state.scraping_result = None
if "scraping_logs" not in st.session_state:
    st.session_state.scraping_logs = []

# ============================================================
# ヘッダー
# ============================================================
st.title("📈 リアルタイム株価ウォッチャー")

# Seleniumの説明
st.info("""
💡 **このページでは Selenium を使ったWebスクレイピングを体験できます！**

**Seleniumとは？**
- 自動でブラウザを操作できるPythonライブラリです
- 人間が見ているのと同じWebページからデータを取得できます
- JavaScriptで動的に生成されるコンテンツも取得可能です

**注意点**
- スクレイピングは対象サイトの利用規約を確認してから行いましょう
- 過度なアクセスはサーバーに負荷をかけるため控えましょう
- Chrome / ChromeDriver が必要です
""")

st.divider()

# ============================================================
# スクレイピング実行セクション
# ============================================================
st.header("🔄 データ取得")

# 2カラムレイアウト
col_button, col_option = st.columns([1, 2])

with col_button:
    start_scraping = st.button("🚀 スクレイピング開始", type="primary", use_container_width=True)

with col_option:
    use_mock = st.checkbox("モックデータを使用（Selenium不要）", value=False)

# スクレイピング実行
if start_scraping:
    # ログをクリア
    st.session_state.scraping_logs = []

    # 進捗バーとステータス表示
    progress_bar = st.progress(0)
    status_container = st.status("スクレイピング中...", expanded=True)

    # 進捗コールバック関数
    def update_progress(progress: float, message: str):
        progress_bar.progress(progress)
        status_container.write(f"✅ {message}")
        st.session_state.scraping_logs.append(message)

    # スクレイピング実行
    if use_mock:
        # モックデータを使用
        update_progress(0.3, "モックデータを準備中...")
        update_progress(0.7, "データを生成中...")
        result = get_mock_data()
        update_progress(1.0, "完了！")
    else:
        # 実際にスクレイピング
        result = scrape_nikkei(progress_callback=update_progress)

    # 結果を保存
    st.session_state.scraping_result = result

    # ステータス更新
    if result["success"]:
        status_container.update(label="✅ スクレイピング完了！", state="complete")
    else:
        status_container.update(label="⚠️ エラーが発生しました", state="error")

    st.balloons()

st.divider()

# ============================================================
# 結果表示セクション
# ============================================================
if st.session_state.scraping_result:
    result = st.session_state.scraping_result

    # モックデータの場合は警告表示
    if result.get("is_mock", False):
        st.warning("📢 " + result.get("message", "モックデータを表示しています"))

    st.header("📊 取得データ")

    # メトリック表示
    col1, col2, col3, col4 = st.columns(4)

    data = result["data"]

    with col1:
        st.metric(
            label="📈 日経平均株価",
            value=data.get("current_price", "N/A")
        )

    with col2:
        change = data.get("price_change", "N/A")
        # 符号に応じて色を変える
        delta_color = "normal"
        if change and change.startswith("-"):
            delta_color = "inverse"
        st.metric(
            label="📉 前日比",
            value=change,
            delta=data.get("price_change_percent", "N/A"),
            delta_color=delta_color
        )

    with col3:
        st.metric(
            label="📊 出来高",
            value=data.get("volume", "N/A")
        )

    with col4:
        st.metric(
            label="🕐 取得時刻",
            value=data.get("timestamp", "N/A").split(" ")[-1] if data.get("timestamp") else "N/A"
        )

    st.divider()

    # ============================================================
    # グラフ表示
    # ============================================================
    st.header("📈 株価推移グラフ")

    # 履歴データをDataFrameに変換
    history = result.get("history", [])
    if history:
        history_df = pd.DataFrame(history)

        # 折れ線グラフ
        fig = px.line(
            history_df,
            x="date",
            y="price",
            title="日経平均株価 推移",
            labels={"date": "日付", "price": "株価（円）"},
            markers=True
        )
        fig.update_layout(
            xaxis_title="日付",
            yaxis_title="株価（円）",
            hovermode="x unified"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ============================================================
    # データテーブル表示
    # ============================================================
    st.header("📋 取得データ一覧")

    # データをテーブル形式で表示
    table_data = {
        "項目": ["現在値", "前日比", "変化率", "出来高", "取得時刻"],
        "値": [
            data.get("current_price", "N/A"),
            data.get("price_change", "N/A"),
            data.get("price_change_percent", "N/A"),
            data.get("volume", "N/A"),
            data.get("timestamp", "N/A")
        ]
    }
    table_df = pd.DataFrame(table_data)
    st.dataframe(table_df, use_container_width=True, hide_index=True)

    st.divider()

    # ============================================================
    # CSVダウンロード
    # ============================================================
    st.header("💾 データダウンロード")

    # ダウンロード用のCSVを作成
    download_df = pd.DataFrame([data])

    # CSVに変換
    csv = download_df.to_csv(index=False, encoding="utf-8-sig")

    # ダウンロードボタン
    col_dl1, col_dl2 = st.columns(2)

    with col_dl1:
        st.download_button(
            label="📥 現在のデータをCSVでダウンロード",
            data=csv,
            file_name=f"nikkei_data_{data.get('timestamp', '').replace(' ', '_').replace(':', '-')}.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col_dl2:
        # 履歴データのダウンロード
        if history:
            history_csv = history_df.to_csv(index=False, encoding="utf-8-sig")
            st.download_button(
                label="📥 履歴データをCSVでダウンロード",
                data=history_csv,
                file_name="nikkei_history.csv",
                mime="text/csv",
                use_container_width=True
            )

    st.divider()

    # ============================================================
    # 処理ログ表示
    # ============================================================
    with st.expander("📋 処理ログを見る"):
        for log in st.session_state.scraping_logs:
            st.write(f"• {log}")

else:
    # まだスクレイピングしていない場合
    st.info("👆 「スクレイピング開始」ボタンをクリックしてデータを取得してください。")

    # サンプル表示
    with st.expander("📖 実装のコードを見る"):
        st.code('''
# スクレイパーの使い方

from scraper.nikkei_scraper import scrape_nikkei

# 進捗コールバック関数
def update_progress(progress, message):
    print(f"[{progress*100:.0f}%] {message}")

# スクレイピング実行
result = scrape_nikkei(progress_callback=update_progress)

# 結果を使用
if result["success"]:
    print(f"現在値: {result['data']['current_price']}")
    print(f"前日比: {result['data']['price_change']}")
        ''', language="python")

st.divider()

# ============================================================
# 学習完了セクション
# ============================================================
st.header("🎉 学習完了！")
st.markdown("""
おめでとうございます！Streamlit学習アプリのすべてのコンテンツを完了しました！

**学んだこと：**
- ✅ 基本コンポーネント（ボタン、入力、選択など）
- ✅ レイアウト（カラム、タブ、エキスパンダーなど）
- ✅ データ表示（DataFrame、グラフ、地図など）
- ✅ Seleniumを使ったスクレイピングと可視化

**次のステップ：**
- 自分のプロジェクトでStreamlitを使ってみましょう
- 公式ドキュメント: https://docs.streamlit.io
- Streamlit Gallery: https://streamlit.io/gallery
""")

st.success("🚀 これであなたもStreamlitマスター！素敵なアプリを作ってください！")
