# プニャンワールド Web改修版

Python 3が必要です。ZIPをすべて展開して、Windowsならrun_web.bat、macOS/Linuxならrun_web.shを実行します。または、このフォルダで python3 run_web.py を実行してください。

http://localhost:8080 をブラウザで開きます。index.htmlの直接ダブルクリックでは起動しません。終了はサーバーの画面でCtrl+C。

Godot 4.3の元Webランタイムに改修PCKを組み込んでいます。同じPCKをネイティブGodotで起動・検証済みですが、ブラウザのWASM実行・IndexedDB・スマホ実機は未検証です。PS5級の商用完成版ではありません。

既存Webセーブを使う場合は同じ配信元URLを保って更新してください。localhostや別URLには古いブラウザの保存データは自動移行されません。ブラウザのサイトデータを消去しないでください。

ダンジョン1: 矢印/WASD/タップ、Space待機、Z攻撃。ダンジョン2: 左右/A・D移動、Spaceジャンプ、Z攻撃、X/Shiftダッシュ。タッチパッド、画面向き、軽量描画、画面揺れ軽減はゲームの設定から操作できます。

詳細は同梱のREPORT.mdを参照してください。
