import os
import time


def qmasq(a, b):
    return a + b

def qmenosq(c, d):
    return c - d

def qporq(e, f):
    return e * f

def qdividq(g, h):
    return g / h



while True:
    os.system('cls' if os.name=='nt' else 'clear')
    decisión = input("Que quieres calcular?\na) Sumas\nb) Restas\nc) Multiplicaciones\nd) Divisiones\n\n-x to Leave\n- ")
    if decisión == "a":
        os.system('cls' if os.name=='nt' else 'clear')
        numeroa = int(input("Primer número para tu suma: "))
        numerob = int(input("Segundo número para tu suma: "))

        resultado = qmasq(numeroa, numerob)

        print(resultado)
        input("Presiona /ENTER\ para volver al menú principal:\n- ")

    elif decisión == "b":
        os.system('cls' if os.name=='nt' else 'clear')
        numeroc = int(input("Primer número para tu resta: "))
        numerod = int(input("Segundo número para tu resta: "))

        resultado = qmenosq(numeroc, numerod)

        print(resultado)
        input("Presiona /ENTER\ para volver al menú principal:\n- ")

    elif decisión == "c":
        os.system('cls' if os.name=='nt' else 'clear')
        numeroe = int(input("Primer número para tu multiplicación: "))
        numerof = int(input("Segundo número para tu multiplicación: "))

        resultado = qporq(numeroe, numerof)

        print(resultado)
        input("Presiona /ENTER\ para volver al menú principal:\n- ")

    elif decisión == "d":
        os.system('cls' if os.name=='nt' else 'clear')
        numerog = int(input("Primer número para tu división: "))
        numeroh = int(input("Segundo número para tu división: "))

        resultado = qdividq(numerog, numeroh)

        print(resultado)
        input("Presiona /ENTER\ para volver al menú principal:\n- ")

    elif decisión == "x":
        os.system('cls' if os.name=='nt' else 'clear')
        break

    else:
        input("Parece que te has equivocado de opción...\n\nPulsa /ENTER\ para volver al menú.\n- ")
        os.system('cls' if os.name=='nt' else 'clear')
print("Gracias por usar SHITTY CALCULATOR\n\nAquí te dejo el GitHub del Creador (dlordmdia): \n\nhttps://github.com/dlordmdia")