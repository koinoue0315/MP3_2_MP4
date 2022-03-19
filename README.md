# MP3 to MP4

## Features
音声ファイルと静止画1枚から動画を作成する

## Requirement
- python 3.x
- ffmpeg 2022-03-17-git-242c07982a-full_build-www.gyan.dev

## Installation

```bash
pip install mutagen
```

## Usage
input_audioフォルダにmp4化したいファイルを配置して下記コマンドを実行する


```
python script.py
```

生成されたmp4ファイルはoutputディレクトリに出力される

## Refrenrace
- [FFmpegでの音声ファイルと静止画1枚からの動画の作成方法](https://dev.classmethod.jp/articles/ffmpeg-create-movie-by-audio/)

## 更新履歴
- 2022/3/19
    - script.batの作成
    - 動画背景画像更新（1920x1080）
    - ffmpegコマンドの更新