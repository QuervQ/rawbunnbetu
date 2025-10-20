import os
import shutil
import exifread
from datetime import datetime

# CR2ファイルがあるフォルダ
source_folder = '/Volumes/EOS_DIGITAL/DCIM/100EOS7D'
# 整理後の保存先（同じでもOK）
output_folder = '/Volumes/RIKIMARU SSD/sandisk/photo/organized'

for filename in os.listdir(source_folder):
    if filename.lower().endswith('.cr2'):
        filepath = os.path.join(source_folder, filename)

        # CR2ファイルをバイナリで開く
        with open(filepath, 'rb') as f:
            tags = exifread.process_file(f, stop_tag="EXIF DateTimeOriginal")

        date_taken = tags.get("EXIF DateTimeOriginal")

        if date_taken:
            # 日付を「YYYY-MM-DD」に整形
            date_str = str(date_taken).split(" ")[0].replace(":", "-")
            dest_dir = os.path.join(output_folder, date_str)

            # フォルダがなければ作成
            os.makedirs(dest_dir, exist_ok=True)

            # ファイルを移動
            shutil.move(filepath, os.path.join(dest_dir, filename))
            print(f"Moved {filename} to {dest_dir}")
        else:
            print(f"Date not found for {filename}, skipping.")
