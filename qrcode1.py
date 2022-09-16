import qrcode
img = qrcode.make('Tu Texto aquí')
type(img)  # qrcode.image.pil.PilImage
img.save("tu_nombre.png")