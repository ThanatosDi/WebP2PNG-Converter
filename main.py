import os
import sys
import shutil
from app.image import ImageConvert
from app.zip import ZIP

def zip_convert(file_path: str):
    try:
        ZIP().decompress(file_path)
        files = ZIP().file_list(file_path)
        for img_path in files:
            ImageConvert().convert(img_path)
            os.remove(img_path)
        ZIP().compress(f'{file_path}')
    except Exception as e:
        print(e)
        sys.exit(1)
    else:
        shutil.rmtree(f'{file_path}_files')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("缺少輸入檔案路徑")
        sys.exit(1)
    file_paths = sys.argv[1:]
    for file_path in file_paths:
        if file_path.endswith('.webp'):
            ImageConvert().convert(file_path)
        if file_path.endswith('.zip'):
            zip_convert(file_path)