import os
import shutil

# フォルダリスト（MF11からMF18、MF21からMF28、MM1からMM8までのフォルダを指定）
folders = [f"../FF{i}/output_files" for i in range(1, 9)] + \
          [f"../MF{i}/output_files" for i in range(11, 19)] + \
          [f"../MF{i}/output_files" for i in range(21, 29)] + \
          [f"../MM{i}/output_files" for i in range(1, 9)]

# 目的地のディレクトリ
destination_dir = "../all_output_files"  # ここを任意の移動先に変更してください

# 目的地フォルダが存在しない場合は作成
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# 各フォルダの.mp4ファイルを移動
for folder in folders:
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            if filename.endswith(".mp4"):
                source_path = os.path.join(folder, filename)
                destination_path = os.path.join(destination_dir, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved: {source_path} to {destination_path}")
    else:
        print(f"Folder not found: {folder}")

print("すべてのファイルの移動が完了しました。")
