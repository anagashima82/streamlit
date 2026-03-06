# ============================================================
# 03_データ表示.py - Streamlitでデータを表示する方法を学ぶ
# ============================================================
import streamlit as st
import pandas as pd
import plotly.express as px

# ページ設定
st.set_page_config(page_title="データ表示", page_icon="📊", layout="wide")

# ============================================================
# session_stateの初期化
# ============================================================
if "filter_category" not in st.session_state:
    st.session_state.filter_category = "全て"
if "filter_min_sales" not in st.session_state:
    st.session_state.filter_min_sales = 0

# ============================================================
# サンプルデータの作成
# ============================================================
@st.cache_data
def create_sample_data():
    """サンプルDataFrameを生成"""
    data = {
        "商品名": ["りんご", "バナナ", "オレンジ", "ぶどう", "メロン", "いちご", "桃", "梨"],
        "カテゴリ": ["果物", "果物", "果物", "果物", "果物", "果物", "果物", "果物"],
        "価格": [150, 100, 200, 400, 800, 500, 300, 250],
        "売上数": [120, 200, 80, 50, 30, 150, 90, 70],
        "在庫": [50, 100, 30, 20, 10, 40, 35, 25],
        "評価": [4.2, 4.5, 4.0, 4.8, 4.3, 4.9, 4.1, 3.9]
    }
    return pd.DataFrame(data)

# 日本の主要都市データ
@st.cache_data
def create_city_data():
    """日本の主要都市の緯度経度データを生成"""
    cities = {
        "都市": ["東京", "大阪", "名古屋", "札幌", "福岡", "仙台", "広島", "神戸"],
        "lat": [35.6762, 34.6937, 35.1815, 43.0618, 33.5902, 38.2682, 34.3853, 34.6901],
        "lon": [139.6503, 135.5023, 136.9066, 141.3545, 130.4017, 140.8694, 132.4553, 135.1956],
        "人口（万人）": [1396, 275, 233, 197, 160, 109, 120, 153]
    }
    return pd.DataFrame(cities)

# 時系列データ
@st.cache_data
def create_time_series_data():
    """時系列データを生成"""
    import numpy as np
    dates = pd.date_range("2024-01-01", periods=30, freq="D")
    data = {
        "日付": dates,
        "売上A": np.random.randint(100, 500, 30).cumsum(),
        "売上B": np.random.randint(80, 400, 30).cumsum(),
        "売上C": np.random.randint(50, 300, 30).cumsum()
    }
    return pd.DataFrame(data)

# データ読み込み
df = create_sample_data()
city_df = create_city_data()
time_df = create_time_series_data()

# ============================================================
# ヘッダー
# ============================================================
st.title("📊 データ表示")
st.markdown("Streamlitでデータを表示・可視化する方法を学びましょう！")

# ============================================================
# DataFrameの表示
# ============================================================
st.header("📋 DataFrameの表示")

# --- st.dataframe ---
st.subheader("📋 インタラクティブテーブル (st.dataframe)")
st.info("💡 **st.dataframe**はソートやフィルタができるインタラクティブなテーブルです。大量のデータを探索するのに便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
import pandas as pd

# サンプルデータ
df = pd.DataFrame({
    "商品名": ["りんご", "バナナ", "オレンジ"],
    "価格": [150, 100, 200],
    "売上数": [120, 200, 80]
})

# インタラクティブテーブル
st.dataframe(df, use_container_width=True)
    ''', language="python")

st.dataframe(df, use_container_width=True)
st.markdown("**💡 機能**: 列ヘッダーをクリックでソート、セルの検索が可能")
st.divider()

# --- st.table ---
st.subheader("📋 静的テーブル (st.table)")
st.info("💡 **st.table**はシンプルな静的テーブルです。小さなデータを見やすく表示したい時に使います。")
with st.expander("📖 このコードを見る"):
    st.code('''
# 静的テーブル（ソート不可）
st.table(df.head(3))
    ''', language="python")

st.table(df.head(3))
st.markdown("**💡 特徴**: シンプルで軽量、小規模データ向け")
st.divider()

# ============================================================
# JSONの表示
# ============================================================
st.header("📝 JSON表示")

st.subheader("📝 JSON表示 (st.json)")
st.info("💡 **st.json**はJSONデータを見やすく表示します。APIレスポンスの確認などに便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
json_data = {
    "name": "山田太郎",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "city": "東京",
        "zip": "100-0001"
    }
}
st.json(json_data)
    ''', language="python")

json_data = {
    "name": "山田太郎",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "city": "東京",
        "zip": "100-0001"
    }
}
st.json(json_data)
st.divider()

# ============================================================
# グラフ表示（Plotly）
# ============================================================
st.header("📈 グラフ表示 (Plotly)")

# --- 折れ線グラフ ---
st.subheader("📈 折れ線グラフ")
st.info("💡 **plotly.express.line**は時系列データの推移を見るのに最適です。複数系列の比較もできます。")
with st.expander("📖 このコードを見る"):
    st.code('''
import plotly.express as px

# 時系列データの折れ線グラフ
fig = px.line(
    time_df,
    x="日付",
    y=["売上A", "売上B", "売上C"],
    title="日別売上推移"
)
st.plotly_chart(fig, use_container_width=True)
    ''', language="python")

fig_line = px.line(
    time_df,
    x="日付",
    y=["売上A", "売上B", "売上C"],
    title="日別売上推移"
)
st.plotly_chart(fig_line, use_container_width=True)
st.divider()

# --- 棒グラフ ---
st.subheader("📊 棒グラフ")
st.info("💡 **plotly.express.bar**はカテゴリ別の比較に最適です。値の大小が一目でわかります。")
with st.expander("📖 このコードを見る"):
    st.code('''
import plotly.express as px

# 棒グラフ
fig = px.bar(
    df,
    x="商品名",
    y="売上数",
    color="商品名",
    title="商品別売上数"
)
st.plotly_chart(fig, use_container_width=True)
    ''', language="python")

fig_bar = px.bar(
    df,
    x="商品名",
    y="売上数",
    color="商品名",
    title="商品別売上数"
)
st.plotly_chart(fig_bar, use_container_width=True)
st.divider()

# --- 散布図 ---
st.subheader("📍 散布図")
st.info("💡 **plotly.express.scatter**は2つの変数の関係を見るのに使います。相関関係の発見に役立ちます。")
with st.expander("📖 このコードを見る"):
    st.code('''
import plotly.express as px

# 散布図
fig = px.scatter(
    df,
    x="価格",
    y="売上数",
    size="在庫",
    color="商品名",
    title="価格 vs 売上数（バブルサイズ=在庫）"
)
st.plotly_chart(fig, use_container_width=True)
    ''', language="python")

fig_scatter = px.scatter(
    df,
    x="価格",
    y="売上数",
    size="在庫",
    color="商品名",
    title="価格 vs 売上数（バブルサイズ=在庫）",
    hover_data=["評価"]
)
st.plotly_chart(fig_scatter, use_container_width=True)
st.divider()

# ============================================================
# 地図表示
# ============================================================
st.header("🗺️ 地図表示")

st.subheader("🗺️ 地図 (st.map)")
st.info("💡 **st.map**は緯度経度データを地図上に表示します。位置情報の可視化に便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
import pandas as pd

# 日本の主要都市
city_df = pd.DataFrame({
    "都市": ["東京", "大阪", "名古屋", "札幌", "福岡"],
    "lat": [35.6762, 34.6937, 35.1815, 43.0618, 33.5902],
    "lon": [139.6503, 135.5023, 136.9066, 141.3545, 130.4017]
})

st.map(city_df)
    ''', language="python")

st.write("**日本の主要都市**")
st.dataframe(city_df[["都市", "人口（万人）"]], use_container_width=True)
st.map(city_df)
st.divider()

# ============================================================
# session_stateを使ったフィルタリング
# ============================================================
st.header("🔍 データフィルタリング（session_state）")

st.info("💡 **st.session_state**を使うと、フィルター状態を保持できます。ページをまたいでも値が維持されます。")
with st.expander("📖 このコードを見る"):
    st.code('''
import streamlit as st

# session_stateの初期化
if "filter_min_sales" not in st.session_state:
    st.session_state.filter_min_sales = 0

# フィルターUI
min_sales = st.slider(
    "最小売上数",
    0, 200, st.session_state.filter_min_sales,
    key="filter_min_sales"
)

# フィルタリング
filtered_df = df[df["売上数"] >= min_sales]
st.dataframe(filtered_df)
    ''', language="python")

# フィルターUI
col1, col2 = st.columns(2)

with col1:
    min_sales = st.slider(
        "最小売上数でフィルタ",
        0, 200,
        st.session_state.filter_min_sales,
        key="filter_min_sales"
    )

with col2:
    min_price = st.slider(
        "最小価格でフィルタ",
        0, 800,
        0,
        key="filter_min_price"
    )

# フィルタリング実行
filtered_df = df[(df["売上数"] >= min_sales) & (df["価格"] >= min_price)]

# 結果表示
st.write(f"**フィルタ結果**: {len(filtered_df)}件 / {len(df)}件")
st.dataframe(filtered_df, use_container_width=True)

# フィルタ後のグラフ
if len(filtered_df) > 0:
    fig_filtered = px.bar(
        filtered_df,
        x="商品名",
        y="売上数",
        color="価格",
        title="フィルタ後の売上数"
    )
    st.plotly_chart(fig_filtered, use_container_width=True)
else:
    st.warning("条件に一致するデータがありません")

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
