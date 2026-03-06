# ============================================================
# 02_レイアウト.py - Streamlitのレイアウト機能を学ぶ
# ============================================================
import streamlit as st

# ページ設定
st.set_page_config(page_title="レイアウト", page_icon="📐", layout="wide")

# ============================================================
# ヘッダー
# ============================================================
st.title("📐 レイアウト")
st.markdown("Streamlitでコンポーネントを配置する方法を学びましょう！")

# ============================================================
# カラム（columns）セクション
# ============================================================
st.header("📊 カラム (st.columns)")

# --- 2列レイアウト ---
st.subheader("📏 2列レイアウト")
st.info("💡 **st.columns**は画面を横に分割できます。2列レイアウトは左右に情報を並べたい時に便利です。")
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

st.markdown("**💡 使用例**: 入力フォームとプレビューを横に並べる、2つの比較データを表示する")
st.divider()

# --- 3列レイアウト ---
st.subheader("📏 3列レイアウト")
st.info("💡 3列に分割すると、より多くの情報を横に並べられます。ダッシュボードのKPI表示などに最適です。")
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

st.markdown("**💡 使用例**: ダッシュボードのKPI、3つの選択肢を並べる")
st.divider()

# --- 比率指定 ---
st.subheader("📏 比率指定カラム")
st.info("💡 カラムの幅を比率で指定できます。サイドバー的な狭いカラムとメインコンテンツを分けたい時に使います。")
with st.expander("📖 このコードを見る"):
    st.code('''
# 1:3の比率で分割
col_side, col_main = st.columns([1, 3])

with col_side:
    st.write("サイド")
    option = st.selectbox("選択", ["A", "B", "C"])

with col_main:
    st.write("メインコンテンツ")
    st.write(f"選択された値: {option}")
    ''', language="python")

col_side, col_main = st.columns([1, 3])
with col_side:
    st.write("サイド")
    option = st.selectbox("選択", ["A", "B", "C"], key="ratio_select")
with col_main:
    st.write("メインコンテンツ")
    st.write(f"選択された値: {option}")

st.markdown("**💡 使用例**: フィルターパネル＋結果表示、ナビゲーション＋コンテンツ")
st.divider()

# ============================================================
# エキスパンダー（expander）セクション
# ============================================================
st.header("📂 エキスパンダー (st.expander)")

st.subheader("📁 折りたたみパネル")
st.info("💡 **st.expander**はクリックで開閉できる折りたたみパネルです。詳細情報を隠しておきたい時に便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
with st.expander("詳細を見る"):
    st.write("ここに詳細な情報を書きます")
    st.write("クリックすると表示されます")
    st.image("https://via.placeholder.com/300x100")
    ''', language="python")

with st.expander("📖 詳細を見る（クリックしてね）"):
    st.write("ここに詳細な情報を書きます")
    st.write("クリックすると表示されます")
    st.markdown("**マークダウン**も使えます！")

st.markdown("**💡 使用例**: FAQ、コードの表示、追加オプションの表示")
st.divider()

# ============================================================
# タブ（tabs）セクション
# ============================================================
st.header("📑 タブ (st.tabs)")

st.subheader("📑 タブUI")
st.info("💡 **st.tabs**は複数のコンテンツをタブで切り替えられます。関連する情報をまとめて見せたい時に便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
tab1, tab2, tab3 = st.tabs(["📊 グラフ", "📋 データ", "⚙️ 設定"])

with tab1:
    st.write("ここにグラフを表示")

with tab2:
    st.write("ここにデータテーブルを表示")

with tab3:
    st.write("ここに設定項目を表示")
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
    st.slider("表示件数", 10, 100, 50, key="tab_slider")

st.markdown("**💡 使用例**: 入力と結果の切り替え、複数形式のデータ表示")
st.divider()

# ============================================================
# サイドバー（sidebar）セクション
# ============================================================
st.header("📎 サイドバー (st.sidebar)")

st.subheader("📎 サイドバーにウィジェット配置")
st.info("💡 **st.sidebar**を使うと、左側のサイドバーにウィジェットを配置できます。フィルターや設定に最適です。")
with st.expander("📖 このコードを見る"):
    st.code('''
# サイドバーにウィジェットを配置
st.sidebar.header("フィルター設定")
category = st.sidebar.selectbox("カテゴリ", ["全て", "A", "B", "C"])
min_value = st.sidebar.slider("最小値", 0, 100, 0)

# メインエリアで使用
st.write(f"カテゴリ: {category}, 最小値: {min_value}")
    ''', language="python")

# 実際にサイドバーに配置
st.sidebar.header("🔧 フィルター設定")
sidebar_category = st.sidebar.selectbox("カテゴリ", ["全て", "A", "B", "C"], key="sidebar_cat")
sidebar_min = st.sidebar.slider("最小値", 0, 100, 0, key="sidebar_min")

st.write(f"サイドバーで選択した値 → カテゴリ: {sidebar_category}, 最小値: {sidebar_min}")

st.markdown("**💡 使用例**: データのフィルタリング、表示設定、ナビゲーション")
st.divider()

# ============================================================
# コンテナ（container）セクション
# ============================================================
st.header("📦 コンテナ (st.container)")

st.subheader("📦 コンテナでグループ化")
st.info("💡 **st.container**は要素をグループ化できます。後から中身を更新したい時にも使います。")
with st.expander("📖 このコードを見る"):
    st.code('''
# コンテナを作成
container = st.container()

# コンテナの外に書いても、後からコンテナに追加できる
st.write("これはコンテナの外")

# コンテナの中に追加
container.write("これはコンテナの中（後から追加）")
container.write("コンテナ内の2行目")
    ''', language="python")

container = st.container(border=True)
st.write("これはコンテナの外")
container.write("これはコンテナの中（後から追加）")
container.write("コンテナ内の2行目")

st.markdown("**💡 使用例**: 動的にコンテンツを追加したい場合、要素のグループ化")
st.divider()

# ============================================================
# 空要素（empty）セクション
# ============================================================
st.header("⬜ 空要素 (st.empty)")

st.subheader("⬜ 動的に更新可能な要素")
st.info("💡 **st.empty**は後から内容を置き換えられるプレースホルダーです。リアルタイム更新に便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
import time

placeholder = st.empty()

# 3秒カウントダウン
for i in range(3, 0, -1):
    placeholder.write(f"カウントダウン: {i}")
    time.sleep(1)

placeholder.write("スタート！")
    ''', language="python")

import time

if st.button("カウントダウン開始", key="countdown_btn"):
    placeholder = st.empty()
    for i in range(3, 0, -1):
        placeholder.write(f"⏱️ カウントダウン: {i}")
        time.sleep(1)
    placeholder.write("🚀 スタート！")

st.markdown("**💡 使用例**: ライブ更新、ローディング表示の置き換え、アニメーション")
st.divider()

# ============================================================
# レイアウトの組み合わせ例
# ============================================================
st.header("🎨 レイアウトの組み合わせ例")

st.info("💡 複数のレイアウト要素を組み合わせると、より複雑なUIを作れます。")
with st.expander("📖 このコードを見る"):
    st.code('''
# 2カラムレイアウト
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("設定")
    data_type = st.radio("データ種類", ["売上", "顧客", "在庫"])
    show_chart = st.checkbox("グラフを表示")

with col2:
    # タブで切り替え
    tab_data, tab_detail = st.tabs(["データ", "詳細"])

    with tab_data:
        st.write(f"{data_type}データを表示中...")
        if show_chart:
            st.line_chart([1, 3, 2, 4, 5])

    with tab_detail:
        with st.expander("詳細情報"):
            st.write("詳細な情報がここに表示されます")
    ''', language="python")

# 実際のデモ
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("設定")
    data_type = st.radio("データ種類", ["売上", "顧客", "在庫"], key="combo_radio")
    show_chart = st.checkbox("グラフを表示", key="combo_checkbox")

with col2:
    tab_data, tab_detail = st.tabs(["データ", "詳細"])

    with tab_data:
        st.write(f"📈 {data_type}データを表示中...")
        if show_chart:
            st.line_chart([1, 3, 2, 4, 5, 4, 6])

    with tab_detail:
        with st.expander("📋 詳細情報"):
            st.write("詳細な情報がここに表示されます")
            st.write("複数のレイアウトを組み合わせると表現の幅が広がります！")

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
