#!/usr/bin/python3

from qrcode_generator import qr_gen
from csv_reader import csv_reader
from file_compressor import *

qr_gen("www.facebook.com")

qr_gen("www.facebook.com", 15, 6, "yellow", "green")

result = csv_reader("C:/Users/zachyzon/Documents/Development/python/mycode/attemptlogin/logs.txt")
print(result)

result2 = zip_directory('C:/Users/zachyzon/Documents/Development/python/zach_yusuf_qr_project/encoded_qrcode_img',
                        'C:/Users/zachyzon/Documents/Development/python/zach_yusuf_qr_project/mockdownloadfolder')
print(result2)
