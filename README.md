# Web版(iPhone Safari / Android Chrome / PCブラウザ)

## 遊び方(いちばん簡単)
1. `web_build/` の中身(index.html など一式)を、HTTPSで公開できる場所に置く(GitHub Pages が簡単)。
2. スマホでそのURLを開く。**横向き**で遊ぶのがおすすめ。
3. 画面右下に仮想十字キー・決定・戻るなどのボタンが出る(タッチ画面の端末では自動)。PCでは右上の「操作」で出し入れ。PCはキーボード(矢印/WASD, Space, Z, X, C, M, Esc, Enter)もそのまま使える。

## GitHub Pages に公開する手順
- A) 手動: `web_build/` の中身をリポジトリの `docs/` か `gh-pages` ブランチに置き、Settings > Pages で公開元を指定。`.nojekyll` を一緒に置くこと。
- B) 自動: このプロジェクトごとGitHubへpush(`.github/workflows/pages.yml` が Godot 4.3 で書き出して公開)。Settings > Pages > Source を「GitHub Actions」に。

## 作り(Web用の設定)
- Godot 4.3 / `gl_compatibility`(WebGL2)/ **スレッドなし**(`variant/thread_support=false`)。GitHub Pages は SharedArrayBuffer 用のヘッダーを付けられないため。
- 日本語フォントは同梱(`assets/fonts/NotoSansJP-subset.otf`、SIL OFL。使う文字だけに絞った版)。Web版はスマホのフォントを使えないため。
- セーブはブラウザの保存領域(IndexedDB)。ブラウザのデータを消すとセーブも消える。
- 音は、画面を最初にタップするまで鳴らない(ブラウザの決まり)。

## 書き出し直し
Godot 4.3 と Web用の書き出しテンプレート(4.3.stable)を入れて:
`godot --headless --path . --export-release Web build/web/index.html`
