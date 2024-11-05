import pandas as pd

# CSVファイルを読み込みます（ファイル名を指定してください）
df = pd.read_csv('./files_with_sets.csv')

#  並び替えたい列に基づいて昇順でソート
df_sorted = df.sort_values(by='Row', ascending=True)

# ソート結果を新しいCSVファイルとして保存
df_sorted.to_csv('sorted_file4.csv', index=False)

