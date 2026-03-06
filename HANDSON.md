# Streamlit学習アプリ ハンズオン手順書

このドキュメントでは、VSCodeを使ってStreamlit学習アプリを一から構築する手順を説明します。

**前提条件**
- Python 3.8以上がインストール済み
- VSCodeがインストール済み
- Google Chrome（スクレイピング機能を使う場合）

---

## 目次

1. [プロジェクトの準備](#1-プロジェクトの準備)
2. [Step 1: メインアプリの作成](#2-step-1-メインアプリの作成)
3. [Step 2: 基本コンポーネントページの作成](#3-step-2-基本コンポーネントページの作成)
4. [Step 3: レイアウトページの作成](#4-step-3-レイアウトページの作成)
5. [Step 4: データ表示ページの作成](#5-step-4-データ表示ページの作成)
6. [Step 5: スクレイパーの作成](#6-step-5-スクレイパーの作成)
7. [Step 6: スクレイピング可視化ページの作成](#7-step-6-スクレイピング可視化ページの作成)
8. [動作確認](#8-動作確認)
9. [トラブルシューティング](#9-トラブルシューティング)

---

## 1. プロジェクトの準備

### 1.1 VSCodeでプロジェクトフォルダを開く

1. VSCodeを起動
2. `ファイル` → `フォルダーを開く` を選択
3. 新しいフォルダ `streamlit_learning` を作成して開く

### 1.2 ターミナルを開く

VSCode上部メニューから:
- `ターミナル` → `新しいターミナル`

または、ショートカット:
- Mac: `` Ctrl + ` ``
- Windows: `` Ctrl + ` ``

### 1.3 仮想環境の作成

ターミナルで以下を実行:

```bash
# 仮想環境を作成
python3 -m venv venv
```

### 1.4 仮想環境を有効化

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

プロンプトの先頭に `(venv)` が表示されれば成功です。

### 1.5 VSCodeでPythonインタープリターを選択

1. `Cmd + Shift + P`（Mac）または `Ctrl + Shift + P`（Windows）でコマンドパレットを開く
2. `Python: Select Interpreter` と入力
3. `./venv/bin/python` を選択

### 1.6 requirements.txt を作成

1. VSCodeのエクスプローラーで右クリック → `新しいファイル`
2. ファイル名: `requirements.txt`
3. 以下の内容を入力して保存:

```
streamlit>=1.32.0
selenium>=4.18.0
webdriver-manager>=4.0.0
pandas>=2.0.0
plotly>=5.18.0
requests>=2.31.0
```

### 1.7 パッケージをインストール

ターミナルで実行:

```bash
pip install -r requirements.txt
```

### 1.8 フォルダ構造を作成

ターミナルで実行:

```bash
mkdir pages scraper
touch scraper/__init__.py
```

**Windowsの場合:**
```bash
mkdir pages
mkdir scraper
type nul > scraper\__init__.py
```

または、VSCodeのエクスプローラーで右クリック → `新しいフォルダー` でも作成できます。

---

## 2. Step 1: メインアプリの作成

### 2.1 app.py を作成

1. エクスプローラーで右クリック → `新しいファイル`
2. ファイル名: `app.py`
3. 以下のコードを入力:

```python
# ============================================================
# app.py - Streamlit学習用メインアプリ
# ============================================================
import streamlit as st

# ページ設定（タイトルとアイコン）
st.set_page_config(
    page_title="Streamlit学習アプリ",
    page_icon="📚",
    layout="wide"
)

# ------------------------------------------------------------
# サイドバー：ナビゲーション説明
# ------------------------------------------------------------
st.sidebar.title("📚 Streamlit学習")
st.sidebar.markdown("""
このアプリでStreamlitの基本を学びましょう！

**学習ページ一覧：**
1. 📦 基本コンポーネント
2. 📐 レイアウト
3. 📊 データ表示
4. 📈 スクレイピング可視化

左のメニューから各ページに移動できます。
""")

# ------------------------------------------------------------
# トップページ：学習の流れ
# ------------------------------------------------------------
st.title("🎓 Streamlit学習アプリへようこそ！")

st.markdown("""
このアプリは**Pythonプログラミング初級者**向けに、
Streamlitの基本から実践的なスクレイピング可視化まで学べる教材です。
""")

# ステップ形式のUI
st.header("📖 学習の流れ")

# ステップ1
st.subheader("Step 1: 基本コンポーネント")
st.markdown("""
- ボタン、テキスト入力、セレクトボックスなどの基本的なUI部品を学びます
- 各コンポーネントのコード例と実際の動作を確認できます
""")

# ステップ2
st.subheader("Step 2: レイアウト")
st.markdown("""
- カラムやタブを使ったページレイアウトの作り方を学びます
- 見やすく使いやすいUIの構築方法を理解できます
""")

# ステップ3
st.subheader("Step 3: データ表示")
st.markdown("""
- pandasのDataFrameをStreamlitで表示する方法を学びます
- plotlyを使ったグラフ作成・地図表示を体験できます
""")

# ステップ4
st.subheader("Step 4: スクレイピング可視化（メインコンテンツ）")
st.markdown("""
- Seleniumを使ったWebスクレイピングの実践
- 取得したデータのリアルタイム可視化
- CSVダウンロード機能の実装
""")

# 区切り線
st.divider()

# 始め方の案内
st.info("👈 **左のサイドバーから「基本コンポーネント」を選んで学習を始めましょう！**")

# フッター
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
```

### 2.2 動作確認

ターミナルで実行:

```bash
streamlit run app.py
```

ブラウザが自動で開きます。開かない場合は http://localhost:8501 にアクセス。

**確認ポイント:**
- タイトル「Streamlit学習アプリへようこそ！」が表示される
- 左サイドバーにナビゲーションが表示される

確認後、ターミナルで `Ctrl + C` を押してサーバーを停止します。

---

## 3. Step 2: 基本コンポーネントページの作成

### 3.1 01_基本コンポーネント.py を作成

1. `pages` フォルダを右クリック → `新しいファイル`
2. ファイル名: `01_基本コンポーネント.py`
3. 以下のコードを入力:

```python
# ============================================================
# 01_基本コンポーネント.py - Streamlitの基本的なUI部品を学ぶ
# ============================================================
import streamlit as st
import time
from datetime import datetime, date

# ページ設定
st.set_page_config(page_title="基本コンポーネント", page_icon="📦", layout="wide")

# ============================================================
# ヘッダー
# ============================================================
st.title("📦 基本コンポーネント")
st.markdown("Streamlitで使える基本的なUI部品（コンポーネント）を学びましょう！")

# ============================================================
# テキスト表示セクション
# ============================================================
st.header("📝 テキスト表示")

# --- st.title ---
st.subheader("🔤 タイトル (st.title)")
st.info("💡 **st.title**はページの一番大きな見出しです。通常、各ページの最上部に1つだけ使います。")
with st.expander("📖 このコードを見る"):
    st.code('''st.title("これがタイトルです")''', language="python")
st.title("これがタイトルです")
st.divider()

# --- st.header ---
st.subheader("📋 ヘッダー (st.header)")
st.info("💡 **st.header**はセクションの見出しに使います。タイトルより少し小さい文字で表示されます。")
with st.expander("📖 このコードを見る"):
    st.code('''st.header("これがヘッダーです")''', language="python")
st.header("これがヘッダーです")
st.divider()

# --- st.write ---
st.subheader("✏️ 汎用出力 (st.write)")
st.info("💡 **st.write**は何でも表示できる万能関数です。文字列、数値、DataFrame、グラフなど、様々なものを表示できます。")
with st.expander("📖 このコードを見る"):
    st.code('''
st.write("文字列を表示")
st.write(123)  # 数値も表示できる
st.write({"キー": "値"})  # 辞書も表示できる
    ''', language="python")
st.write("文字列を表示")
st.write(123)
st.write({"キー": "値"})
st.divider()

# ============================================================
# 入力セクション
# ============================================================
st.header("⌨️ 入力")

# --- st.button ---
st.subheader("🔘 ボタン (st.button)")
st.info("💡 **ボタン**はクリックするとTrueを返します。if文と組み合わせて使います。")
with st.expander("📖 このコードを見る"):
    st.code('''
if st.button("クリックしてね"):
    st.write("ボタンが押されました！")
    ''', language="python")
if st.button("クリックしてね"):
    st.write("ボタンが押されました！")
st.divider()

# --- st.text_input ---
st.subheader("📝 テキスト入力 (st.text_input)")
st.info("💡 **st.text_input**は1行のテキストを入力できるフィールドです。")
with st.expander("📖 このコードを見る"):
    st.code('''
name = st.text_input("お名前を入力してください")
if name:
    st.write(f"こんにちは、{name}さん！")
    ''', language="python")
name = st.text_input("お名前を入力してください")
if name:
    st.write(f"こんにちは、{name}さん！")
st.divider()

# --- st.number_input ---
st.subheader("🔢 数値入力 (st.number_input)")
st.info("💡 **st.number_input**は数値を入力できるフィールドです。最小値・最大値・ステップを設定できます。")
with st.expander("📖 このコードを見る"):
    st.code('''
age = st.number_input("年齢を入力", min_value=0, max_value=120, value=20)
st.write(f"あなたは{age}歳ですね！")
    ''', language="python")
age = st.number_input("年齢を入力", min_value=0, max_value=120, value=20)
st.write(f"あなたは{age}歳ですね！")
st.divider()

# ============================================================
# 選択セクション
# ============================================================
st.header("☑️ 選択")

# --- st.selectbox ---
st.subheader("📋 セレクトボックス (st.selectbox)")
st.info("💡 **st.selectbox**はドロップダウンから1つ選択できます。")
with st.expander("📖 このコードを見る"):
    st.code('''
fruit = st.selectbox(
    "好きな果物を選んでください",
    ["りんご", "バナナ", "オレンジ", "ぶどう"]
)
st.write(f"選んだ果物: {fruit}")
    ''', language="python")
fruit = st.selectbox(
    "好きな果物を選んでください",
    ["りんご", "バナナ", "オレンジ", "ぶどう"]
)
st.write(f"選んだ果物: {fruit}")
st.divider()

# --- st.checkbox ---
st.subheader("☑️ チェックボックス (st.checkbox)")
st.info("💡 **st.checkbox**はオン/オフを切り替えられます。設定や同意確認に便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
agree = st.checkbox("利用規約に同意します")
if agree:
    st.success("同意いただきありがとうございます！")
else:
    st.warning("同意が必要です")
    ''', language="python")
agree = st.checkbox("利用規約に同意します")
if agree:
    st.success("同意いただきありがとうございます！")
else:
    st.warning("同意が必要です")
st.divider()

# ============================================================
# スライダーセクション
# ============================================================
st.header("🎚️ スライダー")

st.subheader("🔢 スライダー (st.slider)")
st.info("💡 **st.slider**はドラッグで値を選択できます。")
with st.expander("📖 このコードを見る"):
    st.code('''
volume = st.slider("音量を設定", min_value=0, max_value=100, value=50)
st.write(f"音量: {volume}%")
    ''', language="python")
volume = st.slider("音量を設定", min_value=0, max_value=100, value=50)
st.write(f"音量: {volume}%")
st.divider()

# ============================================================
# フィードバックセクション
# ============================================================
st.header("💬 フィードバック")

st.subheader("⏳ 進捗バーとスピナー")
st.info("💡 **st.progress**は進捗状況をバーで表示します。**st.spinner**は処理中のメッセージを表示します。")
with st.expander("📖 このコードを見る"):
    st.code('''
if st.button("処理を開始"):
    progress_bar = st.progress(0)
    with st.spinner("処理中..."):
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
    st.success("完了しました！")
    ''', language="python")
if st.button("処理を開始"):
    progress_bar = st.progress(0)
    with st.spinner("処理中..."):
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
    st.success("完了しました！")
st.divider()

# ============================================================
# 次のステップ
# ============================================================
st.header("🚀 次のステップ")
st.markdown("""
基本コンポーネントの学習お疲れさまでした！

**次は「レイアウト」ページで、これらのコンポーネントを上手に配置する方法を学びましょう。**

👈 サイドバーから「レイアウト」を選んでください。
""")
```

### 3.2 動作確認

```bash
streamlit run app.py
```

サイドバーから「基本コンポーネント」を選択して動作を確認します。

---

## 4. Step 3: レイアウトページの作成

### 4.1 02_レイアウト.py を作成

1. `pages` フォルダを右クリック → `新しいファイル`
2. ファイル名: `02_レイアウト.py`
3. 以下のコードを入力:

```python
# ============================================================
# 02_レイアウト.py - Streamlitのレイアウト機能を学ぶ
# ============================================================
import streamlit as st

# ページ設定
st.set_page_config(page_title="レイアウト", page_icon="📐", layout="wide")

st.title("📐 レイアウト")
st.markdown("Streamlitでコンポーネントを配置する方法を学びましょう！")

# ============================================================
# カラム（columns）セクション
# ============================================================
st.header("📊 カラム (st.columns)")

st.subheader("📏 2列レイアウト")
st.info("💡 **st.columns**は画面を横に分割できます。")
with st.expander("📖 このコードを見る"):
    st.code('''
col1, col2 = st.columns(2)

with col1:
    st.write("左のカラム")
    st.button("左のボタン")

with col2:
    st.write("右のカラム")
    st.button("右のボタン")
    ''', language="python")

col1, col2 = st.columns(2)
with col1:
    st.write("左のカラム")
    st.button("左のボタン", key="left_btn")
with col2:
    st.write("右のカラム")
    st.button("右のボタン", key="right_btn")
st.divider()

# 3列でメトリック表示
st.subheader("📏 3列レイアウト（メトリック表示）")
st.info("💡 3列に分割すると、ダッシュボードのKPI表示に最適です。")
with st.expander("📖 このコードを見る"):
    st.code('''
col1, col2, col3 = st.columns(3)
col1.metric("売上", "100万円", "+10%")
col2.metric("訪問者", "5,000人", "+5%")
col3.metric("成約率", "3.2%", "-0.3%")
    ''', language="python")

col1, col2, col3 = st.columns(3)
col1.metric("売上", "100万円", "+10%")
col2.metric("訪問者", "5,000人", "+5%")
col3.metric("成約率", "3.2%", "-0.3%")
st.divider()

# ============================================================
# タブ（tabs）セクション
# ============================================================
st.header("📑 タブ (st.tabs)")

st.info("💡 **st.tabs**は複数のコンテンツをタブで切り替えられます。")
with st.expander("📖 このコードを見る"):
    st.code('''
tab1, tab2, tab3 = st.tabs(["📊 グラフ", "📋 データ", "⚙️ 設定"])

with tab1:
    st.write("ここにグラフを表示")
with tab2:
    st.write("ここにデータを表示")
with tab3:
    st.write("ここに設定を表示")
    ''', language="python")

tab1, tab2, tab3 = st.tabs(["📊 グラフ", "📋 データ", "⚙️ 設定"])

with tab1:
    st.write("ここにグラフを表示")
    st.line_chart([1, 3, 2, 4, 3, 5])

with tab2:
    st.write("ここにデータテーブルを表示")
    st.dataframe({"名前": ["田中", "佐藤", "鈴木"], "点数": [80, 90, 85]})

with tab3:
    st.write("ここに設定項目を表示")
    st.checkbox("通知を受け取る", key="tab_notification")
st.divider()

# ============================================================
# 次のステップ
# ============================================================
st.header("🚀 次のステップ")
st.markdown("""
レイアウトの学習お疲れさまでした！

**次は「データ表示」ページで、DataFrameやグラフの表示方法を学びましょう。**

👈 サイドバーから「データ表示」を選んでください。
""")
```

---

## 5. Step 4: データ表示ページの作成

### 5.1 03_データ表示.py を作成

1. `pages` フォルダを右クリック → `新しいファイル`
2. ファイル名: `03_データ表示.py`
3. 以下のコードを入力:

```python
# ============================================================
# 03_データ表示.py - Streamlitでデータを表示する方法を学ぶ
# ============================================================
import streamlit as st
import pandas as pd
import plotly.express as px

# ページ設定
st.set_page_config(page_title="データ表示", page_icon="📊", layout="wide")

# ============================================================
# サンプルデータの作成
# ============================================================
@st.cache_data
def create_sample_data():
    """サンプルDataFrameを生成"""
    data = {
        "商品名": ["りんご", "バナナ", "オレンジ", "ぶどう", "メロン"],
        "価格": [150, 100, 200, 400, 800],
        "売上数": [120, 200, 80, 50, 30],
    }
    return pd.DataFrame(data)

df = create_sample_data()

# ============================================================
# ヘッダー
# ============================================================
st.title("📊 データ表示")
st.markdown("Streamlitでデータを表示・可視化する方法を学びましょう！")

# ============================================================
# DataFrameの表示
# ============================================================
st.header("📋 DataFrameの表示")

st.subheader("📋 インタラクティブテーブル (st.dataframe)")
st.info("💡 **st.dataframe**はソートやフィルタができるテーブルです。")
with st.expander("📖 このコードを見る"):
    st.code('''
import pandas as pd

df = pd.DataFrame({
    "商品名": ["りんご", "バナナ", "オレンジ"],
    "価格": [150, 100, 200],
    "売上数": [120, 200, 80]
})
st.dataframe(df, use_container_width=True)
    ''', language="python")
st.dataframe(df, use_container_width=True)
st.divider()

# ============================================================
# グラフ表示（Plotly）
# ============================================================
st.header("📈 グラフ表示 (Plotly)")

st.subheader("📊 棒グラフ")
st.info("💡 **plotly.express.bar**はカテゴリ別の比較に最適です。")
with st.expander("📖 このコードを見る"):
    st.code('''
import plotly.express as px

fig = px.bar(df, x="商品名", y="売上数", color="商品名", title="商品別売上数")
st.plotly_chart(fig, use_container_width=True)
    ''', language="python")

fig_bar = px.bar(df, x="商品名", y="売上数", color="商品名", title="商品別売上数")
st.plotly_chart(fig_bar, use_container_width=True)
st.divider()

# ============================================================
# session_stateを使ったフィルタリング
# ============================================================
st.header("🔍 データフィルタリング")

st.info("💡 スライダーでデータをフィルタリングできます。")

min_sales = st.slider("最小売上数でフィルタ", 0, 200, 0)
filtered_df = df[df["売上数"] >= min_sales]

st.write(f"**フィルタ結果**: {len(filtered_df)}件")
st.dataframe(filtered_df, use_container_width=True)
st.divider()

# ============================================================
# 次のステップ
# ============================================================
st.header("🚀 次のステップ")
st.markdown("""
データ表示の学習お疲れさまでした！

**次は「スクレイピング可視化」ページで、実際にWebからデータを取得して可視化する方法を学びましょう。**

👈 サイドバーから「スクレイピング可視化」を選んでください。
""")
```

---

## 6. Step 5: スクレイパーの作成

### 6.1 nikkei_scraper.py を作成

1. `scraper` フォルダを右クリック → `新しいファイル`
2. ファイル名: `nikkei_scraper.py`
3. 以下のコードを入力:

```python
# ============================================================
# nikkei_scraper.py - Yahoo!ファイナンスから日経平均株価を取得
# ============================================================
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import re


def get_mock_data() -> dict:
    """
    スクレイピング失敗時に返すモックデータ
    """
    return {
        "success": True,
        "is_mock": True,
        "data": {
            "current_price": "38,500.25",
            "price_change": "+350.75",
            "price_change_percent": "+0.92%",
            "volume": "N/A",
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
        "message": "モックデータを使用しています"
    }


def scrape_nikkei(progress_callback=None) -> dict:
    """
    Yahoo!ファイナンスから日経平均株価データを取得

    Args:
        progress_callback: 進捗を通知するコールバック関数
                          float(0.0〜1.0)とstr(ステータスメッセージ)を受け取る
    """

    def notify_progress(progress: float, message: str):
        if progress_callback:
            progress_callback(progress, message)

    driver = None

    try:
        # ステップ1: ブラウザ起動準備
        notify_progress(0.1, "ブラウザを起動中...")

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

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
        time.sleep(2)

        # ステップ4: データ取得
        notify_progress(0.7, "データを取得中...")

        # 初期値
        current_price = "取得失敗"
        price_change = "取得失敗"
        price_change_percent = "取得失敗"
        volume = "N/A"

        # 株価を取得
        try:
            price_element = driver.find_element(
                By.CSS_SELECTOR, "span[class*='PriceBoard__price']"
            )
            current_price = price_element.text.strip()

            # 前日比を含む親ブロックを取得
            price_block = driver.find_element(
                By.CSS_SELECTOR, "div[class*='PriceBoard__priceBlock']"
            )
            block_text = price_block.text

            # 前日比を正規表現で抽出
            change_match = re.search(
                r'([+-]?[0-9,]+\.[0-9]+)\s*\(([+-]?[0-9]+\.[0-9]+%)\)',
                block_text
            )
            if change_match:
                price_change = change_match.group(1)
                price_change_percent = change_match.group(2)
        except Exception:
            pass

        notify_progress(0.9, "データ整形中...")

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
        notify_progress(1.0, f"エラー発生: {str(e)}")
        mock_data = get_mock_data()
        mock_data["message"] = f"スクレイピングに失敗しました。モックデータを表示します。"
        return mock_data

    finally:
        if driver:
            driver.quit()
```

---

## 7. Step 6: スクレイピング可視化ページの作成

### 7.1 04_スクレイピング可視化.py を作成

1. `pages` フォルダを右クリック → `新しいファイル`
2. ファイル名: `04_スクレイピング可視化.py`
3. 以下のコードを入力:

```python
# ============================================================
# 04_スクレイピング可視化.py - Seleniumでスクレイピングしてデータを可視化
# ============================================================
import streamlit as st
import pandas as pd
import plotly.express as px
import sys
from pathlib import Path

# scraperモジュールをインポート
sys.path.append(str(Path(__file__).parent.parent))
from scraper.nikkei_scraper import scrape_nikkei, get_mock_data

# ページ設定
st.set_page_config(page_title="スクレイピング可視化", page_icon="📈", layout="wide")

# session_stateの初期化
if "scraping_result" not in st.session_state:
    st.session_state.scraping_result = None

# ============================================================
# ヘッダー
# ============================================================
st.title("📈 リアルタイム株価ウォッチャー")

st.info("""
💡 **このページでは Selenium を使ったWebスクレイピングを体験できます！**

**注意点**
- スクレイピングは対象サイトの利用規約を確認してから行いましょう
- Chrome / ChromeDriver が必要です
""")

st.divider()

# ============================================================
# スクレイピング実行セクション
# ============================================================
st.header("🔄 データ取得")

col_button, col_option = st.columns([1, 2])

with col_button:
    start_scraping = st.button("🚀 スクレイピング開始", type="primary")

with col_option:
    use_mock = st.checkbox("モックデータを使用（Selenium不要）", value=False)

# スクレイピング実行
if start_scraping:
    progress_bar = st.progress(0)
    status_container = st.status("スクレイピング中...", expanded=True)

    def update_progress(progress: float, message: str):
        progress_bar.progress(progress)
        status_container.write(f"✅ {message}")

    if use_mock:
        update_progress(0.5, "モックデータを準備中...")
        result = get_mock_data()
        update_progress(1.0, "完了！")
    else:
        result = scrape_nikkei(progress_callback=update_progress)

    st.session_state.scraping_result = result

    if result["success"]:
        status_container.update(label="✅ スクレイピング完了！", state="complete")
    st.balloons()

st.divider()

# ============================================================
# 結果表示セクション
# ============================================================
if st.session_state.scraping_result:
    result = st.session_state.scraping_result

    if result.get("is_mock", False):
        st.warning("📢 " + result.get("message", "モックデータを表示しています"))

    st.header("📊 取得データ")

    # メトリック表示
    col1, col2, col3 = st.columns(3)
    data = result["data"]

    with col1:
        st.metric(label="📈 日経平均株価", value=data.get("current_price", "N/A"))

    with col2:
        st.metric(
            label="📉 前日比",
            value=data.get("price_change", "N/A"),
            delta=data.get("price_change_percent", "N/A")
        )

    with col3:
        st.metric(label="🕐 取得時刻", value=data.get("timestamp", "N/A").split(" ")[-1])

    st.divider()

    # グラフ表示
    st.header("📈 株価推移グラフ")
    history = result.get("history", [])
    if history:
        history_df = pd.DataFrame(history)
        fig = px.line(history_df, x="date", y="price", title="日経平均株価 推移", markers=True)
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # CSVダウンロード
    st.header("💾 データダウンロード")
    download_df = pd.DataFrame([data])
    csv = download_df.to_csv(index=False, encoding="utf-8-sig")
    st.download_button(
        label="📥 CSVでダウンロード",
        data=csv,
        file_name="nikkei_data.csv",
        mime="text/csv"
    )

else:
    st.info("👆 「スクレイピング開始」ボタンをクリックしてデータを取得してください。")

st.divider()

# ============================================================
# 学習完了
# ============================================================
st.header("🎉 学習完了！")
st.success("🚀 これであなたもStreamlitマスター！素敵なアプリを作ってください！")
```

---

## 8. 動作確認

### 8.1 最終的なフォルダ構造

VSCodeのエクスプローラーで以下の構造になっていることを確認:

```
streamlit_learning/
├── app.py
├── pages/
│   ├── 01_基本コンポーネント.py
│   ├── 02_レイアウト.py
│   ├── 03_データ表示.py
│   └── 04_スクレイピング可視化.py
├── scraper/
│   ├── __init__.py
│   └── nikkei_scraper.py
├── requirements.txt
└── venv/
```

### 8.2 アプリの起動

ターミナルで実行:

```bash
streamlit run app.py
```

### 8.3 確認項目

| ページ | 確認内容 |
|-------|---------|
| トップページ | 学習の流れが表示される |
| 基本コンポーネント | ボタン、入力、スライダーが動作する |
| レイアウト | カラム、タブが正しく表示される |
| データ表示 | グラフとフィルタリングが動作する |
| スクレイピング可視化 | データ取得またはモックデータが表示される |

---

## 9. トラブルシューティング

### ModuleNotFoundError が出る

```bash
pip install -r requirements.txt
```

### スクレイピングがエラーになる

「モックデータを使用」にチェックを入れて学習を継続できます。

### ポートが使用中

```bash
streamlit run app.py --server.port 8502
```

### 仮想環境が有効になっていない

プロンプトに `(venv)` が表示されているか確認。表示されていない場合:

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

---

**お疲れさまでした！** 🎉
