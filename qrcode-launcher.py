import os
import time
import qrcode

while True:
    start = input("\nQue quieres hacer?\n\nCrear -c\nubicar -f\n-x to Leave\n\n-")
    if start == "c":
        text = input("TEXTO PARA EL CÓDIGO QR:\n-")
        img = qrcode.make(text)
        type(img)  
        fname = ("COMO LLAMAR EL ARCHIVO:\n-")
        img.save(f"{fname}.png")

    elif start == "f":
        print("EN CONSTRUCCIÓN. VUELVE MÁS TARDE")
        time.sleep(1)
        #locat = input("Qué archivo quieres encontrar?\nPiensa en la extensión al caso de ser exclusiva o")
        #def find(name, path):
            #for root, dirs, files in os.walk(path):
                #if name in files:
                    #return os.path.join(root, name)
    elif start == "x":
        break