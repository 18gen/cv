# Computer Visionで指をカウント

このプロジェクトでは OpenCV, Mediapipe, CVZone を用いて指の数をウェブカメラを通してカウントします。

参照：[Python：CVZone（OpenCV & MediaPipe）ライブラリを使って指の数をカウントしてみた](https://life-wisdom.xyz/20211207/1721/)

## 事前準備

### macOSの場合
1. **Homebrew** (macOS package manager)  
   Install Homebrew
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Python 3.11
    ***MacOS***
    HomeBrewからPython 3.11 をインストール
    ```bash
    brew install python@3.11
    ```
    任意: インストール後、以下のコマンドで確認
    ```bash
    /opt/homebrew/bin/python3.11 --version
    ```

### Windowsの場合
1. Python 3.11
    [公式 Python ウェブサイト](https://www.python.org/downloads/)から Python 3.11 をダウンロードしてインストール。インストール時に「Add Python to PATH」にチェックを入れることを忘れないでください。

   任意: インストール後、以下のコマンドで確認
    ```bash
    python --version
    ```

## セットアップ
1. リポジトリをクローンする
    以下のコマンドでリポジトリをクローンします
    ```bash
    git clone git@github.com:18gen/cv.git
    cd cv
    ```
    Git を使用しない場合は、リポジトリから ZIP ファイルをダウンロードし、解凍してください

2. 仮想環境を作成する

   macOSの場合: Python 3.11 を使用して仮想環境を作成
    ```bash
    /opt/homebrew/bin/python3.11 -m venv venv
    ```
   Windowsの場合: 仮想環境を作成
    ```bash
    python -m venv venv
    ```

4. 仮想環境を有効化する

   macOSの場合
    ```bash
    source venv/bin/activate
    ```
    Windowsの場合
    ```bash
    venv\Scripts\activate
    ```
    仮想環境を終了したい場合
    ```bash
    deactivate
    ```

6. 必要なライブラリをインストールする
    ```bash
    pip install mediapipe opencv-python opencv-python-headless cvzone
    ```
    任意: インストール後、以下のコマンドで確認
    ```bash
    pip list
    ```

7. スクリプトを実行する
    仮想環境内でスクリプトを実行します
    ```bash
    python fingerCount.py
    ```
