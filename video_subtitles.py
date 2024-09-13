import csv
import subprocess
import os
from moviepy.editor import *


def put_on_subtitle(delay_time, defalt_rag, output_file):
    # 動画の158秒から178秒を抜き取る
    clip = VideoFileClip("video001_peach_vs_daisy.mp4").subclip(158, 175)

    # フォントファイルのパスを指定 (必要に応じて適切な日本語フォントファイルを指定してください)
    font_path = "Noto_Sans_JP/NotoSansJP-VariableFont_wght.ttf"

    # テキストクリップのサイズを設定
    txt_size = (clip.w, 100)  # 幅は動画の幅、高さは100ピクセル

    # 背景色を設定 (RGBA形式、Aはアルファ値で透明度を指定)
    bg_color = (0, 0, 0, 128)  # 半透明の黒
    txt_color = 'white'

    # 1つ目のテキストクリップを作成 (2秒後に表示)
    text1 = "サドンデスなりました\nどっちが勝つのか"
    txt_clip1 = TextClip(text1, font=font_path, fontsize=50, color=txt_color)
    txt_clip1 = txt_clip1.set_pos(('center', 'bottom')).set_duration(1.746).set_start(2.258 + delay_time - defalt_rag)
    bg_clip1 = ColorClip(size=(txt_size[0], txt_size[1] + 30), color=bg_color, duration=1.746).set_position(('center', 'bottom')).set_start(2.258 + delay_time - defalt_rag)

    # 2つ目のテキストクリップを作成 (5秒後に表示)
    text2 = "これね野菜を投げつけたいところですが\n投げつけるのにも隙がありますからね"
    txt_clip2 = TextClip(text2, font=font_path, fontsize=50, color=txt_color)
    txt_clip2 = txt_clip2.set_pos(('center', 'bottom')).set_duration(4.122).set_start(5.011 + delay_time - defalt_rag)
    bg_clip2 = ColorClip(size=(txt_size[0], txt_size[1] + 30), color=bg_color, duration=4.122).set_position(('center', 'bottom')).set_start(5.011 + delay_time - defalt_rag)

    # 3つ目のテキストクリップを作成 (9秒後に表示)
    text3 = "でもピーチは技知ってますね"
    txt_clip3 = TextClip(text3, font=font_path, fontsize=50, color=txt_color)
    txt_clip3 = txt_clip3.set_pos(('center', 'bottom')).set_duration(1.828).set_start(9.133 + delay_time - defalt_rag)
    bg_clip3 = ColorClip(size=(txt_size[0], txt_size[1] + 30), color=bg_color, duration=1.828).set_position(('center', 'bottom')).set_start(9.133 + delay_time - defalt_rag)

    # 4つ目のテキストクリップを作成 (11秒後に表示)
    text4 = "カウンターのキノピオで"
    txt_clip4 = TextClip(text4, font=font_path, fontsize=50, color=txt_color)
    txt_clip4 = txt_clip4.set_pos(('center', 'bottom')).set_duration(0.790).set_start(11.331 + delay_time - defalt_rag)
    bg_clip4 = ColorClip(size=(txt_size[0], txt_size[1] + 30), color=bg_color, duration=2.797).set_position(('center', 'bottom')).set_start(11.331 + delay_time - defalt_rag)

    # 5つ目のテキストクリップを作成 (11秒後に表示)
    text5 = "はい野菜ヒット"
    txt_clip5 = TextClip(text5, font=font_path, fontsize=50, color='red')
    txt_clip5 = txt_clip5.set_pos(('center', 'bottom')).set_duration(2.007).set_start(12.121 + delay_time - defalt_rag)
    bg_clip5 = ColorClip(size=(txt_size[0], txt_size[1] + 30), color=bg_color, duration=2.797).set_position(('center', 'bottom')).set_start(11.331 + delay_time - defalt_rag)

    # 映像とテキスト、背景を重ねる
    video = CompositeVideoClip([clip, bg_clip1, txt_clip1, bg_clip2, txt_clip2, bg_clip3, txt_clip3, bg_clip4, txt_clip4, bg_clip5, txt_clip5])

    # 動画として出力する
    video.write_videofile(output_file, codec='libx264')


f1 = open('subtitle_shift_timing.csv', 'r')
delayReader = csv.reader(f1)
next(delayReader)

for delay_row in delayReader:
    put_on_subtitle(float(delay_row[0]), float(delay_row[1]), delay_row[2])
    
f1.close()

