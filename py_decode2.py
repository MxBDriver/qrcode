#Decode
from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open("E-A/qrcode.png"))
print(data)