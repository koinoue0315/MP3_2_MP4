import os
import subprocess
import mutagen
from mutagen.easyid3 import EasyID3

audio_file_dir = os.path.join(os.getcwd(), 'input_audio')
output_file_dir = os.path.join(os.getcwd(), 'output')

background_img = os.path.join(os.getcwd(), 'background.png')
# audioファイル（mp3）ファイル一覧取得
files = os.listdir(audio_file_dir)
audio_files = [f for f in files if (os.path.isfile(os.path.join(audio_file_dir, f)) and 'mp3' in f)]
print(audio_files)
for audio_file in audio_files:
    try:
        audio_file_path = os.path.join(audio_file_dir, audio_file)
        tags = EasyID3(audio_file_path)
        items = tags.items()
        album = items[0][1][0]
        title = items[1][1][0]
    except mutagen.id3._util.ID3NoHeaderError:
        # mp3メタ情報が設定されていない場合のハンドリング
        album = ''
        title = audio_file.replace('.mp3', '')

    out_file_name = f'{album}_{title}.mp4'
    out_file_path = os.path.join(output_file_dir, out_file_name)
    print(album, title)

    command = f'ffmpeg -loop 1 -r 30000/1001 -i "{background_img}" -i "{audio_file_path}" -acodec aac -strict experimental -ab 320k -ac 2 -ar 48000 -c:v libx264 -pix_fmt yuv420p -shortest "{out_file_path}"'
    print(command)
    subprocess.run(command)

    # https://qiita.com/moshi/items/57735f2602aa0cc3b88e
    # https://dev.classmethod.jp/articles/ffmpeg-create-movie-by-audio/