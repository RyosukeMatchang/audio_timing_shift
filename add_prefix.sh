#!/bin/bash

# FF1からFF8まで
for i in {1..8}; do
    prefix="FF$i"
    for file in ../FF$i/output_files/*.mp4; do
        # 新しいファイル名を設定
        new_name="../FF$i/output_files/${prefix}${file##*/}"
        
        # ファイル名を変更
        mv "$file" "$new_name"
    done
done

# MF11からMF18まで
for i in {13..18}; do
    prefix="MF$i"
    for file in ../MF$i/output_files/*.mp4; do
        # 新しいファイル名を設定
        new_name="../MF$i/output_files/${prefix}${file##*/}"
        
        # ファイル名を変更
        mv "$file" "$new_name"
    done
done

# MF21からMF28まで
for i in {21..28}; do
    prefix="MF$i"
    for file in ../MF$i/output_files/*.mp4; do
        # 新しいファイル名を設定
        new_name="../MF$i/output_files/${prefix}${file##*/}"
        
        # ファイル名を変更
        mv "$file" "$new_name"
    done
done

# MM1からMM8まで
for i in {1..8}; do
    prefix="MM$i"
    for file in ../MM$i/output_files/*.mp4; do
        # 新しいファイル名を設定
        new_name="../MM$i/output_files/${prefix}${file##*/}"
        
        # ファイル名を変更
        mv "$file" "$new_name"
    done
done

