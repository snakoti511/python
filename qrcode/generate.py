import qrcode

qrData = "This is a qr text"

qrCodeFileToSave = "qr.png"

qrObject = qrcode.QRCode(border=10)

qrObject.add_data(qrData)

qrObject.make()
image = qrObject.make_image(fill_color="red")
image.save(qrCodeFileToSave)