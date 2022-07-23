import time
import webbrowser

seguir = "y"

print("\n----IDIOTCALCULATOR----\n\n Created by DlordMDia")

time.sleep(1)

while seguir == "y":
    equation = input("\nCuál es tu ecuación? ")
    print(f"Resultado: {eval(equation)}\n")
    seguir = input("Quieres hacer otro calculo? (y/n): ")

time.sleep(1)

#saber mas sobre dlord
print("\nQuieres saber más sobre DlordMDia?")
time.sleep(1)
respuesta2 = input("\n Tu respuesta (y/n): ")

if respuesta2 == "y":
    print("\nDlord tiene muchos perfiles con información y contenido. Te recomiendo su Quizz para saber un poco más de él. Aquí dejo el github de su python code. También te daré a la vez TODOS los medios más interesantes de Dlord!\n ")
    respuesta3 = input("\n Los quieres abrir en tu Browser? (y/n): ")
    if respuesta3 == "y":
        time.sleep(1)
        webbrowser.open("https://github.com/dlordmdia/Practicas_Python/blob/main/dlordrap_quiz.py")
        webbrowser.open("https://www.youtube.com/channel/UCdHXWPzL5MbRSDNexzbTg7w")
        webbrowser.open("https://www.youtube.com/channel/UCUa5cLjlaspHPciMtEZUgZg")

    elif respuesta3 == "p":
        webbrowser.open("https://www.pornhub.com/users/dlordhot")

time.sleep(1)
print("Gracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")