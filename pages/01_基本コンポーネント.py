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

# --- st.subheader ---
st.subheader("📌 サブヘッダー (st.subheader)")
st.info("💡 **st.subheader**はヘッダーの下位の見出しです。細かいセクション分けに便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''st.subheader("これがサブヘッダーです")''', language="python")
st.subheader("これがサブヘッダーです")
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

# --- st.markdown ---
st.subheader("📄 マークダウン (st.markdown)")
st.info("💡 **st.markdown**はマークダウン記法で装飾されたテキストを表示できます。**太字**や*斜体*、リンクなども使えます。")
with st.expander("📖 このコードを見る"):
    st.code('''
st.markdown("**太字**や*斜体*が使えます")
st.markdown("- リスト項目1")
st.markdown("- リスト項目2")
st.markdown("[Streamlit公式サイト](https://streamlit.io)")
    ''', language="python")
st.markdown("**太字**や*斜体*が使えます")
st.markdown("- リスト項目1")
st.markdown("- リスト項目2")
st.markdown("[Streamlit公式サイト](https://streamlit.io)")
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
st.info("💡 **st.text_input**は1行のテキストを入力できるフィールドです。ユーザーからの入力を受け取るのに使います。")
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

# --- st.text_area ---
st.subheader("📋 テキストエリア (st.text_area)")
st.info("💡 **st.text_area**は複数行のテキストを入力できます。長い文章やコメントの入力に便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
message = st.text_area("メッセージを入力", height=100)
if message:
    st.write(f"入力された文字数: {len(message)}文字")
    ''', language="python")
message = st.text_area("メッセージを入力", height=100)
if message:
    st.write(f"入力された文字数: {len(message)}文字")
st.divider()

# ============================================================
# 選択セクション
# ============================================================
st.header("☑️ 選択")

# --- st.selectbox ---
st.subheader("📋 セレクトボックス (st.selectbox)")
st.info("💡 **st.selectbox**はドロップダウンから1つ選択できます。選択肢が多い場合に便利です。")
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

# --- st.multiselect ---
st.subheader("📋 マルチセレクト (st.multiselect)")
st.info("💡 **st.multiselect**は複数の項目を選択できます。タグの選択などに便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
colors = st.multiselect(
    "好きな色を選んでください（複数可）",
    ["赤", "青", "緑", "黄", "紫"]
)
st.write(f"選んだ色: {colors}")
    ''', language="python")
colors = st.multiselect(
    "好きな色を選んでください（複数可）",
    ["赤", "青", "緑", "黄", "紫"]
)
st.write(f"選んだ色: {colors}")
st.divider()

# --- st.radio ---
st.subheader("🔘 ラジオボタン (st.radio)")
st.info("💡 **st.radio**は選択肢を一覧表示して1つ選択できます。選択肢が少ない場合に見やすいです。")
with st.expander("📖 このコードを見る"):
    st.code('''
size = st.radio(
    "サイズを選んでください",
    ["S", "M", "L", "XL"]
)
st.write(f"選んだサイズ: {size}")
    ''', language="python")
size = st.radio(
    "サイズを選んでください",
    ["S", "M", "L", "XL"]
)
st.write(f"選んだサイズ: {size}")
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

# --- st.slider (整数) ---
st.subheader("🔢 整数スライダー (st.slider)")
st.info("💡 **st.slider**はドラッグで値を選択できます。範囲内の数値を直感的に選べます。")
with st.expander("📖 このコードを見る"):
    st.code('''
volume = st.slider("音量を設定", min_value=0, max_value=100, value=50)
st.write(f"音量: {volume}%")
    ''', language="python")
volume = st.slider("音量を設定", min_value=0, max_value=100, value=50)
st.write(f"音量: {volume}%")
st.divider()

# --- st.slider (浮動小数点) ---
st.subheader("🔢 小数スライダー (st.slider)")
st.info("💡 **st.slider**は小数も扱えます。step引数で刻み幅を設定できます。")
with st.expander("📖 このコードを見る"):
    st.code('''
temperature = st.slider(
    "温度を設定（℃）",
    min_value=0.0,
    max_value=40.0,
    value=25.0,
    step=0.5
)
st.write(f"設定温度: {temperature}℃")
    ''', language="python")
temperature = st.slider(
    "温度を設定（℃）",
    min_value=0.0,
    max_value=40.0,
    value=25.0,
    step=0.5
)
st.write(f"設定温度: {temperature}℃")
st.divider()

# ============================================================
# 日付・時刻セクション
# ============================================================
st.header("📅 日付・時刻")

# --- st.date_input ---
st.subheader("📅 日付入力 (st.date_input)")
st.info("💡 **st.date_input**はカレンダーから日付を選択できます。予約や期間指定に便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
selected_date = st.date_input("日付を選択", value=date.today())
st.write(f"選択した日付: {selected_date}")
    ''', language="python")
selected_date = st.date_input("日付を選択", value=date.today())
st.write(f"選択した日付: {selected_date}")
st.divider()

# --- st.time_input ---
st.subheader("⏰ 時刻入力 (st.time_input)")
st.info("💡 **st.time_input**は時刻を選択できます。予約時間の設定などに使います。")
with st.expander("📖 このコードを見る"):
    st.code('''
selected_time = st.time_input("時刻を選択")
st.write(f"選択した時刻: {selected_time}")
    ''', language="python")
selected_time = st.time_input("時刻を選択")
st.write(f"選択した時刻: {selected_time}")
st.divider()

# ============================================================
# ファイルセクション
# ============================================================
st.header("📁 ファイル")

# --- st.file_uploader ---
st.subheader("📤 ファイルアップロード (st.file_uploader)")
st.info("💡 **st.file_uploader**はファイルをアップロードできます。画像やCSVなどの読み込みに使います。")
with st.expander("📖 このコードを見る"):
    st.code('''
uploaded_file = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="アップロードされた画像")
    ''', language="python")
uploaded_file = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="アップロードされた画像")
st.divider()

# ============================================================
# その他セクション
# ============================================================
st.header("🎨 その他")

# --- st.color_picker ---
st.subheader("🎨 カラーピッカー (st.color_picker)")
st.info("💡 **st.color_picker**は色を選択できます。テーマ設定などに便利です。")
with st.expander("📖 このコードを見る"):
    st.code('''
color = st.color_picker("色を選んでください", "#00f900")
st.write(f"選んだ色: {color}")
st.markdown(f'<div style="background-color:{color};padding:20px;">この色です！</div>',
            unsafe_allow_html=True)
    ''', language="python")
color = st.color_picker("色を選んでください", "#00f900")
st.write(f"選んだ色: {color}")
st.markdown(f'<div style="background-color:{color};padding:20px;">この色です！</div>',
            unsafe_allow_html=True)
st.divider()

# --- st.metric ---
st.subheader("📊 メトリック (st.metric)")
st.info("💡 **st.metric**は数値とその変化を表示します。KPIやダッシュボードに最適です。delta引数で増減を表示できます。")
with st.expander("📖 このコードを見る"):
    st.code('''
col1, col2, col3 = st.columns(3)
col1.metric("気温", "25°C", "2°C")
col2.metric("湿度", "60%", "-5%")
col3.metric("風速", "3m/s", "0m/s")
    ''', language="python")
col1, col2, col3 = st.columns(3)
col1.metric("気温", "25°C", "2°C")
col2.metric("湿度", "60%", "-5%")
col3.metric("風速", "3m/s", "0m/s")
st.divider()

# ============================================================
# フィードバックセクション
# ============================================================
st.header("💬 フィードバック")

# --- st.progress + st.spinner ---
st.subheader("⏳ 進捗バーとスピナー (st.progress / st.spinner)")
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

# --- st.success / st.error / st.warning / st.info ---
st.subheader("📢 メッセージボックス")
st.info("💡 4種類のメッセージボックスを使い分けてユーザーに情報を伝えられます。")
with st.expander("📖 このコードを見る"):
    st.code('''
st.success("成功メッセージ: 処理が完了しました！")
st.error("エラーメッセージ: 問題が発生しました")
st.warning("警告メッセージ: 注意が必要です")
st.info("情報メッセージ: お知らせです")
    ''', language="python")
st.success("成功メッセージ: 処理が完了しました！")
st.error("エラーメッセージ: 問題が発生しました")
st.warning("警告メッセージ: 注意が必要です")
st.info("情報メッセージ: お知らせです")
st.divider()

# ============================================================
# エフェクトセクション
# ============================================================
st.header("🎉 エフェクト")

# --- st.balloons / st.snow ---
st.subheader("🎈 バルーンと雪 (st.balloons / st.snow)")
st.info("💡 **st.balloons**と**st.snow**は画面にエフェクトを表示します。お祝いや演出に使えます！")
with st.expander("📖 このコードを見る"):
    st.code('''
if st.button("バルーンを飛ばす"):
    st.balloons()

if st.button("雪を降らせる"):
    st.snow()
    ''', language="python")

col1, col2 = st.columns(2)
with col1:
    if st.button("🎈 バルーンを飛ばす"):
        st.balloons()
with col2:
    if st.button("❄️ 雪を降らせる"):
        st.snow()

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
