import pandas as pd
import random

# CSVファイルを読み込み、元の行番号を保持
df = pd.read_csv('./comment_list2.csv')  # 実際のファイル名に変更してください
df.reset_index(inplace=True)  # 元の行番号を保持
df.rename(columns={'index': 'Row'}, inplace=True)  # 'Row'という列名に変更

# 'filename'列から'delay'の後の数値を抽出し、新しい列 'delay_value' として追加
df['delay_value'] = df['filename'].str.extract(r'delay([\-]?\d+\.\d+)')[0].astype(float)

# 指定された12種類のdelay値
unique_delays = [-1.5, -1.25, -1.0, -0.75, -0.5, 0.0, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
result = []
set_num = 1  # セット番号の初期化

# 各 delay_value を2回ずつ含む24個のセットを作成し、データが足りる限り繰り返す
while True:
    set_group = []

    # 各 delay_value に対して2つのファイルをランダムに選びセットを作成
    for delay in unique_delays:
        delay_group = df[df['delay_value'] == delay]
        
        # 各 delay に対して2つのファイルをランダムに選ぶ
        if len(delay_group) >= 2:
            selected_rows = delay_group.sample(2)
            set_group.extend(selected_rows[['Row', 'filename', 'topic_tag']].values.tolist())
        else:
            # ファイルが足りなくなった場合、セットを破棄して再試行
            set_group = []
            break

    # 重複のチェック
    rows = [row[0] for row in set_group]
    if len(rows) != len(set(rows)):
        # 重複があればセットの作成をやり直す
        continue

    # セットが24個に満たない場合もループを終了
    if len(set_group) < 24:
        break

    # 重複もなく、24個のセットが完成した場合のみ、選択したファイルを元の DataFrame から削除
    for row in rows:
        result.append([row, set_group[rows.index(row)][1], set_group[rows.index(row)][2], f'Set(2){set_num}'])
        df = df[df['Row'] != row]
    
    # セット番号をインクリメント
    set_num += 1

# 結果をDataFrameに変換して保存
output_df = pd.DataFrame(result, columns=['Row', 'Filename', 'topic_tag', 'Set'])
output_df.to_csv('files_with_sets2.csv', index=False)

print("指定された delay 値を2回ずつ含む 24個1セットのファイルが 'files_with_sets2.csv' に保存されました。")
