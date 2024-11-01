import pandas as pd

# CSVファイルを読み込む
file_path = './files_with_sets2.csv'  # ファイルパスを指定
df = pd.read_csv(file_path)

# カウントしたいSet名を指定
set_name = 'Set(2)139'  # Set1, Set2など

# 指定したSetのtopic_tagをカウントする
set_counts = df[df['Set'] == set_name]['topic_tag'].value_counts()

# 結果を表示
print(f"{set_name}のtopic_tagの種類と個数:")
print(set_counts)
