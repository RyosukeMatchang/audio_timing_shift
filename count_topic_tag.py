import os
import pandas as pd

# 処理するディレクトリとファイルパスのリストを生成
directories = [
    f"../FF{i}/audio_commentary_annotations.csv" for i in range(1, 9)
] + [
    f"../MF{i}/audio_commentary_annotations.csv" for i in range(11, 19)
] + [
    f"../MF{i}/audio_commentary_annotations.csv" for i in range(21, 29)
] + [
    f"../MM{i}/audio_commentary_annotations.csv" for i in range(1, 9)
]

# 全てのファイルの topic_tag を累積してカウントするためのシリーズを初期化
total_tag_counts = pd.Series(dtype=int)

# 各ファイルについて topic_tag をカウントし、累積
for file_path in directories:
    # ファイルが存在するか確認してから処理
    if os.path.exists(file_path):
        # CSVファイルを読み込む
        df = pd.read_csv(file_path)

        # 'topic_tag' 列の要素をカウントする
        tag_counts = df['topic_tag'].value_counts()

        # 累積カウントに追加
        total_tag_counts = total_tag_counts.add(tag_counts, fill_value=0)

# 結果の表示（合計）
print("Total tag counts across all files:")
print(total_tag_counts.astype(int))
