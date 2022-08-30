from ast import Add
import time
from tokenize import Triple
import webbrowser
import os

#Start
os.system('cls' if os.name=='nt' else 'clear')

while True:
    Loop = True
    print("\n--DLORD LAUNCHER--\n\n")
    time.sleep(1)

    what1 = input("Qué quieres hacer?\n\na)Ver Contenido de Música\nb)Ver Contenido de Aventuras y Exteriores\nc)Ver Contenido de Drones\n\n-x to Leave\n-")


    if what1 =="a":
        os.system('cls' if os.name=='nt' else 'clear')
        time.sleep(1)
        print("Abriendo...  \n")
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        webbrowser.open("https://www.youtube.com/channel/UCdHXWPzL5MbRSDNexzbTg7w")

    elif what1 == "b":
        os.system('cls' if os.name=='nt' else 'clear')
        time.sleep(1)
        print("Abriendo...  \n")
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        webbrowser.open("https://www.youtube.com/channel/UCC-KnP22oPHfTt_vM4X5_6g")

    elif what1 == "c":
        os.system('cls' if os.name=='nt' else 'clear')
        time.sleep(1)
        print("Abriendo...  \n")
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        webbrowser.open("https://www.youtube.com/channel/UCC-KnP22oPHfTt_vM4X5_6g")
    
    elif what1 == "x":
        os.system('cls' if os.name=='nt' else 'clear')
        break
    
    elif what1 == "h":
        while Loop:
            os.system('cls' if os.name=='nt' else 'clear')
            input("Has descubierto la página oscura de Dlord. Esto Contiene Dar PHO, Dlord Dark, etc.\n/ENTER\ to continue\n- ")
            os.system('cls' if os.name=='nt' else 'clear')
            dark = input("a)Dlord PHO (Música agresiva y violenta)\nb)Dlord Dark (Acciones Ilegales por los exteriores)\n\n-e to get Back\n-x to Leave\n- ")
            if dark == "a":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Canal inactivo... Intentalo más tarde...")
                time.sleep(2)
            elif dark == "b":
                os.system('cls' if os.name=='nt' else 'clear')
                print("Canal inactivo... Intentalo más tarde...")
                time.sleep(2)
            elif dark == "e":
                os.system('cls' if os.name=='nt' else 'clear')
                Loop = False
            else:
                os.system('cls' if os.name=='nt' else 'clear')
                print("Adios...")
                exit()
os.system('cls' if os.name=='nt' else 'clear')
print("Hasta pronto!")
