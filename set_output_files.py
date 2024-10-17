import os
import random
import shutil
from collections import defaultdict
import multiprocessing

# 動画ファイルのディレクトリと出力先フォルダのパス
input_dir = 'all_output_files'
output_dir = 'output_folders'
num_videos_per_set = 25
repeats_per_video = 5

# 動画ファイルを取得
video_files = [f for f in os.listdir(input_dir) if f.endswith('.mp4')]

# delay の値を解析し、動画ファイルを分類するための辞書
delay_values_range = [-1.5, -1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
delay_count = defaultdict(int)

# delayの値をカウント
for video in video_files:
    if "delay" in video:
        try:
            # delayの後の数値を取得
            delay_value = float(video.split("delay")[1].replace('.mp4', ''))
            if delay_value in delay_values_range:
                delay_count[delay_value] += 1
        except ValueError:
            continue

# 動画ファイルを5回ずつリストに追加
video_list = []

# delay の後の数字が少なくとも2回出るようにする処理
for video in video_files:
    if "delay" in video:
        try:
            # delayの後の数値を取得
            delay_value = float(video.split("delay")[1].replace('.mp4', ''))
            if delay_value in delay_values_range:
                if delay_count[delay_value] < 2:
                    # delay の値が2回未満ならリストに追加
                    video_list.extend([video] * 2)
                else:
                    # 通常通り5回追加
                    video_list.extend([video] * repeats_per_video)
        except ValueError:
            # 数値に変換できない場合はスキップ
            continue
    else:
        # delay がない、または範囲外の動画は通常通り5回追加
        video_list.extend([video] * repeats_per_video)

# シャッフルしてランダム順にする
random.shuffle(video_list)

# 必要なセット数を計算
num_sets = len(video_list) // num_videos_per_set

# 出力先フォルダが存在しなければ作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# フォルダに動画を仕分けする関数
def process_video_set(set_number, video_subset):
    set_folder = os.path.join(output_dir, f'set_{set_number+1}')
    os.makedirs(set_folder, exist_ok=True)
    for video_file in video_subset:
        src = os.path.join(input_dir, video_file)
        dst = os.path.join(set_folder, video_file)
        shutil.copy(src, dst)
    print(f'Set {set_number+1} 完了')

# 並列で処理を実行する関数
def distribute_videos_in_parallel(video_list, num_sets, num_videos_per_set):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())  # CPUのコア数に合わせてプロセス数を設定
    for i in range(num_sets):
        video_subset = video_list[i * num_videos_per_set:(i + 1) * num_videos_per_set]
        pool.apply_async(process_video_set, args=(i, video_subset))  # 非同期にプロセスを実行
    pool.close()
    pool.join()  # 全プロセスが終了するまで待機

# 並列処理を実行
distribute_videos_in_parallel(video_list, num_sets, num_videos_per_set)
