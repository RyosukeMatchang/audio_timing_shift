#!/bin/bash

# 移動先のディレクトリ
DESTINATION="../MM8/output_files"

# ディレクトリが存在しない場合は作成
if [ ! -d "$DESTINATION" ]; then
  mkdir -p "$DESTINATION"
  echo "ディレクトリ $DESTINATION を作成しました。"
fi

# output* という名前のファイルを移動
mv ./output* "$DESTINATION"

echo "ファイルを $DESTINATION に移動しました。"
