import qrcode
from PIL import Image,ImageEnhance

# create qrcode
qrcode_text = 'https://github.com/fborges42' # limited to 100 characters
qr = qrcode.QRCode(border=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(qrcode_text)
qr.make()
qrcode_img = qr.make_image()

# make qrcode transparent
qrcode_rgba = qrcode_img.convert('RGBA').resize((186,186))
getData = qrcode_rgba.getdata()
newData = []
for item in getData:
    # replace white pixel for transparent with alpha channel
   if item[0] == 255 and item[1] == 255 and item[2] == 255:
       newData.append((255, 255, 255, 0))
   else:
       newData.append(item)
qrcode_rgba.putdata(newData)
qrcode_rgba.save('data/output/qrcode-transparent-bg.png', 'PNG')

# merge qrcode with bg
with Image.open("data/avatar.png").resize((186,186)) as qrcode_bg:
    enhancer = ImageEnhance.Brightness(qrcode_bg)
    enhanced_im = enhancer.enhance(2.8)
    enhanced_im.paste(qrcode_rgba, (0, 0), qrcode_rgba)
    enhanced_im.convert('RGB').save('data/output/output.png', 'PNG')
