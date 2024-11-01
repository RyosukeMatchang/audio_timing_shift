import pandas as pd
import numpy as np
from scipy.stats import entropy

# グローバル変数 M の設定
MAX = 10  # 任意の値を設定

def count_topic_tag_proportions(df):
    # topic_tagの個数をカウントし、割合を計算
    topic_counts = df['topic_tag'].value_counts(normalize=True)
    
    # 指定されたtopic_tagのキーで辞書を作成し、存在しない場合は0を設定
    topic_proportions_dict = {
        '対戦風景': topic_counts.get('対戦風景', 0),
        'アイテム': topic_counts.get('アイテム', 0),
        'ファイター': topic_counts.get('ファイター', 0),
        '対戦結果': topic_counts.get('対戦結果', 0),
        'アシストフィギュア': topic_counts.get('アシストフィギュア', 0)
    }
    
    return topic_proportions_dict

def calculate_kl_divergence_sum(set_proportions, reference_proportions):
    kl_divergence_sum = 0
    for key in reference_proportions.keys():
        p = reference_proportions[key]
        q = set_proportions[key]
        
        # Q(i) = 0 かつ P(i) > 0 の場合、Mを返す
        if q == 0:
            if key in ('対戦風景', 'アイテム', 'ファイター'):
                kl_divergence_sum += MAX
            continue

        kl_divergence_sum += p * np.log(p / q)
    
    return kl_divergence_sum

# メイン処理
file_path1 = './files_with_sets.csv'  # CSVファイルのパス
file_path2 = './comment_list.csv'  # CSVファイルのパス

df1 = pd.read_csv(file_path1)   # CSVファイルを読み込む
df2 = pd.read_csv(file_path2)   # CSVファイルを読み込む

# df2の全体に対してtopic_tagの割合を計算
reference_proportions = count_topic_tag_proportions(df2)

# Set列の各値ごとにcount_topic_tag_proportionsを適用し、KLダイバージェンスを計算
results = []

for set_value, group_df in df1.groupby('Set'):
    # 各Setのtopic_tag割合を計算
    set_proportions = count_topic_tag_proportions(group_df)
    
    # KLダイバージェンスを計算
    kl_divergence = calculate_kl_divergence_sum(set_proportions, reference_proportions)
    
    # 結果をリストに保存 (Set番号とKLダイバージェンスのみ)
    results.append({'Set': set_value, 'KL Divergence': kl_divergence})

# 結果をデータフレームとして保存
results_df = pd.DataFrame(results)
output_path = './set_kl_divergences.csv'
results_df.to_csv(output_path, index=False)

print(f"結果が '{output_path}' に保存されました。")
