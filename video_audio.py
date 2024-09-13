import csv
import subprocess
import os
import pandas as pd
from pydub import AudioSegment
import tempfile

def determine_trim_timings(num :int, df :DataFrame, delay : float, video_length : float):
    end_time = df['end_time_sec'].iloc[num]
    if end_time - df['start_time_sec'].iloc[num] + delay > video_length:
        return end_time, df['start_time_sec'].iloc[num]
    for k in range(0, num):
    	if end_time - df['start_time_sec'].iloc[num - k] + delay > video_length:
            return end_time, df['start_time_sec'].iloc[num - k + 1]
    return df['start_time_sec'].iloc[num - k], end_time


def cut_video(input_file, output_file, start_time, duration):
    
    ffmpeg_command = [
        'ffmpeg',
        '-y',
        '-ss', start_time,
        '-i', input_file,
        '-t', duration,
        '-c', 'copy',
        output_file
    ]
    try:
        result = subprocess.run(ffmpeg_command, capture_output=True, text=True, check=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")  # エラーメッセージ


def extract_audio(input_file, output_file, start_time, end_time):
    """
    指定された入力ファイルから、指定された時間範囲の部分を切り出して出力ファイルに保存する関数。

    Parameters:
        input_file (str): 入力WAVファイルのパス。
        output_file (str): 出力WAVファイルのパス。
        start_time (float): 切り出しの開始時間（秒単位）。
        end_time (float): 切り出しの終了時間（秒単位）。
    """
    current_directory = os.getcwd() # 現在のディレクトリのパスを取得
    # 相対パスを絶対パスに変換
    input_path = os.path.join(current_directory, input_file)
    output_path = os.path.join(current_directory, output_file)
	# start_timeとend_timeを秒からミリ秒に変換
    start_milli_time = int(start_time * 1000)
    end_milli_time = int(end_time * 1000)

    
    
    try:
        # Pydubでオーディオセグメントを読み込む
        audio = AudioSegment.from_wav(input_path)

        # 切り出し
        extracted = audio[start_milli_time:end_milli_time]

        # 切り出したオーディオを保存
        extracted.export(output_path, format="wav")
    except Exception as e:
        print(f"エラー: {e}")


def merge_audio_and_video(video_file, audio_file, output_file):
    ffmpeg_command = [
        'ffmpeg',
        '-y',
        '-i', video_file,         # 入力ビデオファイル
        '-i', audio_file,         # 入力オーディオファイル
        '-c:v', 'copy',           # ビデオストリームをコピー
        '-c:a', 'aac',            # オーディオストリームをAAC形式でエンコード
        '-b:a', '192k',           # オーディオビットレートを指定
        '-filter:a', 'volume=3.0',# オーディオの音量を3倍にする
        '-map', '0:v:0',          # 最初の入力ファイルのビデオストリームをマッピング
        '-map', '1:a:0',          # 二番目の入力ファイルのオーディオストリームをマッピング
        '-shortest',              # 短い方のストリームに合わせて出力
        output_file               # 出力ファイル
    ]
    
    try:
        result = subprocess.run(ffmpeg_command, capture_output=True, text=True, check=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")


delay_df = pd.read_csv('shift_timing.csv') #path名は絶対でも相対でも可
audio_df = pd.read_csv('')

source_video_file_path = '' #cut前のvideo
source_audio_file_path = ''

for video_csv_num in range():
    start_time, end_time = determine_trim_timings(num :int, df :DataFrame, delay : float, video_length : float)
    for seg_row = next(segReader)
    #現在使っているid,delaytimeを元に最終的な出力ファイル名を決定
    outputfile_path = f"output_id{}_delay{}.mp4"

    # 一時ファイルを作成して、それぞれの関数で使用する
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as video_temp_file, \
        tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as audio_temp_file:
    
        # 一時ファイルのパスを取得
        video_temp_file_path = video_temp_file.name
        audio_temp_file_path = audio_temp_file.name

        #一時ファイルに途中経過を保存
        cut_video(source_video_file_path, video_temp_file_path, start_time, str(cut_time))
        extract_audio(source_audio_file_path, audio_temp_file_path, float(seg_row[2]) - float(delay_row[0]) + float(delay_row[1]), float(seg_row[3]) - float(delay_row[0]) + float(delay_row[1]))

        #出力した一時ファイルを用いて動画を出力
        merge_audio_and_video(video_temp_file_path, audio_temp_file_path, seg_row[4])





# import pandas as pd

# # CSVファイルの読み込み
# df = pd.read_csv('data.csv')

# # データフレームの型を確認
# print(type(df))
