import qrcode
img = qrcode.make('Tu Texto aquí')
type(img)  
img.save("tu_nombre.png")