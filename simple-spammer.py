import os
import time
import pyperclip

while True:
    os.system('cls' if os.name=='nt' else 'clear')
    print("\n--SIMPLE-SPAMMER--\n\n")
    time.sleep(1)
    os.system('cls' if os.name=='nt' else 'clear')
    print("ctr + z to stop programm\n\n")
    what = input("Qué quieres escribir?\n- ")
    much = input ("Cuantas veces?\n- ")

    output = ""

    for i in range(int(much)):
        output += what + " "

    pyperclip.copy(output)
    os.system('cls' if os.name=='nt' else 'clear')
    print("El Spam se ha copiado a tu portapapeles\nctr + v para pegar el mensaje largo")
    time.sleep(2)