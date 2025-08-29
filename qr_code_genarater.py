import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enetr the filename: ')
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color= 'white')
image.save(filename)
image.show()
print(f'QR code is saved as {filename}')

