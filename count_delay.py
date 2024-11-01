import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('combined_output.csv')  # 実際のファイル名に変更してください

# 'filename'列から'delay'の後の数値を抽出し、新しい列 'delay_value' として追加
df['delay_value'] = df['filename'].str.extract(r'delay([\-]?\d+\.\d+)')[0].astype(float)

# delay_valueごとの出現回数をカウント
delay_counts = df['delay_value'].value_counts().sort_index()

# 結果を表示
print(delay_counts)
