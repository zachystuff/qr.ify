#!/usr/bin/python3

# standard library imports
import os      # low-level, operating system agnostic commands (i.e. supports most OSes)
import zipfile  # tools to create, read, write, append, and list a ZIP file


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='a') as zipf:
        len_dir_path = len(folder_path)
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])

    return

