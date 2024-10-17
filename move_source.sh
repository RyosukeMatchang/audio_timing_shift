#!/bin/bash

# 移動先のディレクトリ
DESTINATION="../MM8"

# ディレクトリが存在しない場合は作成
if [ ! -d "$DESTINATION" ]; then
  mkdir -p "$DESTINATION"
  echo "ディレクトリ $DESTINATION を作成しました。"
fi

# ソースのファイルを移動
mv ../smashcorpus_audio/MM/match8/audio_commentary_annotations.csv "$DESTINATION"
mv ../smashcorpus_audio/MM/match8/audio_commentary.wav "$DESTINATION"
mv ../smashcorpus_video/MM/match8/gameplay_video.mp4 "$DESTINATION"
cp ./shift_timing.csv "$DESTINATION"


echo "ファイルを $DESTINATION に移動しました。"
