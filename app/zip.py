import os
import zipfile as zf

from .config import Config


class ZIP():
    def __init__(self): ...

    def compress(self, file_path:str):
        """將轉換後的資料夾內容壓縮回 epub

        Args:
            filename (str): 原始檔案的絕對路徑名稱
        """
        dirname = os.path.dirname(file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(file_path))
        file_list = []
        for root, _dirs, files in os.walk(f'{file_path}_files/'):
            for name in files:
                file_list.append(os.path.join(root, name))
        save_path = os.path.join(dirname, f'{file_name}_new{file_extension}')
        with zf.ZipFile(save_path, 'w', zf.zlib.DEFLATED, compresslevel=Config.ZIP_COMPRESS_LEVEL) as z_f:
            for file in file_list:
                arc_name = file[len(f'{file_path}_files'):]
                z_f.write(file, arc_name)

    def decompress(self, file_path:str):
        """將 epub 解壓縮到資料夾中

        Args:
            file_path (str): 檔案的絕對路徑名稱
        """
        zipfile = zf.ZipFile(file_path)
        path = f'{file_path}_files/'
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)
        for names in zipfile.namelist():
            zipfile.extract(names, path)

    def file_list(self, file_path: str) -> list:
        """取得 epub 的 zipfile 物件

        Args:
            file_path (str): 檔案的絕對路徑名稱

        Returns:
            list: list 物件
        """
        file_name_list = zf.ZipFile(file_path).namelist()
        dir_path = f'{file_path}_files/'
        return [os.path.join(dir_path, file_path) for file_path in file_name_list if os.path.isfile(os.path.join(dir_path, file_path))]