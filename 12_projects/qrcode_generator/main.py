"""
We are going to use a python library like qrcode and convert url to qr
"""

import qrcode

url = input("Enter your url: ")
filename = input("Filename you want to save it as: ")
img = qrcode.make(url)
if not (filename.endswith(".png")):
    filename = filename + ".png"
type(img)
img.save(filename)
