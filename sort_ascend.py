import pandas as pd

# CSVファイルを読み込みます（ファイル名を指定してください）
df = pd.read_csv('./set_kl_divergences2.csv')

#  並び替えたい列に基づいて昇順でソート
df_sorted = df.sort_values(by='KL Divergence', ascending=True)

# ソート結果を新しいCSVファイルとして保存
df_sorted.to_csv('sorted_file2.csv', index=False)

