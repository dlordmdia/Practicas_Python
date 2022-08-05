import time
import os

while True:
    start = input("Qué quieres hacer?\n\na) Modificar información\nb) Ver contenido\nc) Exit\n\n- ")
    if start == "a":
        datamod = open("data.txt", "w")
        datamod.write("Python")
        datamod.close()

    elif start == "b":
        data = open("data.txt", "r").read()
        print(data)
        print("\n")

    elif start == "c":
        break