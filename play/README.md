# プリンワールド ブラウザ版 0.12.12（テスト用）

https://purinyogurtworld-design.github.io/punyan/play/ を開くと遊べます。

- パソコンの Chrome か Edge でどうぞ。
- 最初に読み込むのは約 82 MB（エンジン・タイトル・新しい冒険・プロローグ）だけです。残りの約 347 MB は、プロローグを見ている間に裏で読み込みます（右上に「データ読み込み中」と進み具合が出ます）。
- 読み込みが終わる前に先の場面（王宮の街・続きから・章選択）へ進んだときは、その場で「準備しています」の画面が出て、終わりしだい続きが始まります。
- UI は UI パック（PurinWorld_UI_Complete_2）にまるごと入れ替えています。ゲームパッド（PlayStation / Xbox）でも遊べます。
- 冒険の記録はそのブラウザに残ります（別のブラウザやPCには引き継がれません）。

## ファイル

- `index.html` / `PunyanWorld.js` / `PunyanWorld.wasm` / `PunyanWorld.pck` … 最初に読み込む分
- `pack/rest_00.pck` 〜 `pack/rest_07.pck` … プロローグ中に裏で読み込む残りのデータ
