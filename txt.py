import pandas as pd
import os

# CSVファイルを読み込む
df = pd.read_csv('/home/takamichi-lab3/kenkyu/audio_git/comment_list_with_set_id.csv')  # 'your_file.csv' を実際のファイル名に置き換えてください

# `sequence`フォルダが存在しない場合は作成
output_folder = 'sequence'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# `set_id`ごとにグループ化
grouped = df.groupby('set_id')

# カウンターを初期化
file_counter = 1

# 各グループに対して処理を行う
for set_id, group in grouped:
    # `wave/filename`の形式でリストを作成　waveの場所は適宜変更してください
    filenames = [f"wave/{filename}" for filename in group['filename']]
    
    # 出力ファイル名を生成
    output_filename = os.path.join(output_folder, f"{file_counter:04d}.txt")
    
    # .txtファイルに書き出し
    with open(output_filename, 'w') as f:
        for filename in filenames:
            f.write(f"{filename}\n")
    
    # カウンターをインクリメント
    file_counter += 1
