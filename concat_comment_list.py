import pandas as pd

# CSVファイルの読み込み
df1 = pd.read_csv("./files_with_setsr2.csv")
df2 = pd.read_csv("./files_with_sets.csv")

# df1とdf2のRow列の番号が一致する行をdf2から削除
df2_filtered = df2[~df2['Row'].isin(df1['Row'])]

# 2つのデータを結合（縦方向に結合）
result = pd.concat([df1, df2_filtered], ignore_index=True)

result.to_csv("merged_output.csv", index=False)  # 必要に応じてCSVとして保存
