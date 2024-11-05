import pandas as pd

# 最初のCSVファイルを読み込み
df1 = pd.read_csv('./sorted_file.csv')

# KL Divergence列が0.1以上の行のSet列の値を抽出（0未満も）
set_values = df1[(df1['KL Divergence'] >= 0.1)]['Set'].unique()

# 2番目のCSVファイルを読み込み
df2 = pd.read_csv('./files_with_sets.csv')

# Set列がset_valuesに含まれる行のRow列の値を抽出
row_values = df2[df2['Set'].isin(set_values)]['Row'].unique()

# 3番目のCSVファイルを読み込み
df3 = pd.read_csv('./comment_list.csv')

# row_valuesのインデックスに該当する行を抽出
filtered_rows = df3.loc[row_values]
print(filtered_rows)

# 結果を新しいCSVファイルに保存
filtered_rows.to_csv('comment_list2.csv', index=False)
