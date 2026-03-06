# Streamlit学習アプリ

Pythonプログラミング初級者向けのStreamlit学習教材です。基本コンポーネントからスクレイピング可視化まで、ステップバイステップで学べます。

## 必要な環境

- Python 3.8以上
- Google Chrome（スクレイピング機能を使う場合）
- ChromeDriver（webdriver-managerが自動インストール）

## インストール手順

1. リポジトリをクローン（またはダウンロード）

2. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

## 実行方法

```bash
streamlit run app.py
```

ブラウザが自動で開き、アプリが表示されます。
表示されない場合は http://localhost:8501 にアクセスしてください。

## 学習順序

以下の順番で学習することをおすすめします：

### Step 1: 基本コンポーネント
- ボタン、テキスト入力、セレクトボックスなどの基本UI
- 各コンポーネントのコード例と実際の動作を確認

### Step 2: レイアウト
- カラム、タブ、エキスパンダーなどのレイアウト機能
- 見やすく使いやすいUIの構築方法

### Step 3: データ表示
- pandasのDataFrame表示
- Plotlyを使ったグラフ作成
- 地図表示

### Step 4: スクレイピング可視化（メインコンテンツ）
- Seleniumを使ったWebスクレイピング
- 取得データのリアルタイム可視化
- CSVダウンロード機能

## ファイル構成

```
streamlit/
├── app.py                    # メインアプリ（ナビゲーション）
├── pages/
│   ├── 01_基本コンポーネント.py
│   ├── 02_レイアウト.py
│   ├── 03_データ表示.py
│   └── 04_スクレイピング可視化.py
├── scraper/
│   ├── __init__.py
│   └── nikkei_scraper.py     # Seleniumスクレイパー
├── requirements.txt
└── README.md
```

## 注意事項

### スクレイピングについて
- スクレイピングは対象サイトの利用規約を確認してから行ってください
- 過度なアクセスはサーバーに負荷をかけるため控えてください
- 学習目的以外での使用には十分注意してください

### ChromeDriverについて
- `webdriver-manager`が自動でChromeDriverをダウンロード・管理します
- Chrome本体は事前にインストールしておく必要があります
- スクレイピングがうまくいかない場合は「モックデータを使用」オプションを使ってください

## トラブルシューティング

### Streamlitが起動しない
```bash
pip install --upgrade streamlit
```

### スクレイピングがエラーになる
- Chromeがインストールされているか確認
- 「モックデータを使用」オプションで学習を継続できます

### 日本語が文字化けする
- ターミナル/コンソールのエンコーディングをUTF-8に設定してください

## 参考リンク

- [Streamlit公式ドキュメント](https://docs.streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Selenium公式ドキュメント](https://selenium-python.readthedocs.io/)
