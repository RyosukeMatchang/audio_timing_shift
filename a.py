import pandas as pd

# CSVファイルの読み込み
df1 = pd.read_csv('files_with_sets.csv')
df2 = pd.read_csv('files_with_setsr2.csv')

# Row列の番号が一致する行を抽出（inner join）
merged_df = pd.merge(df1, df2, on='Row')

# 結果をCSVファイルに出力
merged_df.to_csv('matched_rows.csv', index=False)

print("一致する行が 'matched_rows.csv' に出力されました。")
