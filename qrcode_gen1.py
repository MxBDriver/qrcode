import qrcode

def make_qr(filename, msg):
    img = qrcode.make(msg)
    img.save(filename)
    img.show()
    
