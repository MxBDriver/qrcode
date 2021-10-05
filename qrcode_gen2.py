#Genrate
from png import Image
import pyqrcode
from pyqrcode.builder import _get_png_size, _png

url = pyqrcode.create("https://github.com/MxBDriver", error='H')
#print(url.terminal())
print(url.png("E-A/Github.png", scale=6))

