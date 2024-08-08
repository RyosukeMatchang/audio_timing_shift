import csv
import subprocess
import os
import pandas as pd

def determine_trim_timings(num :int, df :DataFrame, delay : float, video_length : float):
    end_time = df['end_time_sec'].iloc[num]
    start_time[num] = df['start_time_sec'].iloc[num]
    if end_time - df['start_time_sec'].iloc[num] + delay > video_length:
        return end_time, df['start_time_sec'].iloc[num]
    for k in range(0, num):
    	if end_time - df['start_time_sec'].iloc[num - k] + delay > video_length:
            return end_time, df['start_time_sec'].iloc[num - k + 1]
    return df['start_time_sec'].iloc[num - k], end_time



import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv('data.csv')

# データフレームの型を確認
print(type(df))

#clear!
print("aa")