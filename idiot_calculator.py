import time

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
    respuesta3 = input("\n Lo quieres? (y/n): \n")
    if respuesta3 == "y":
        time.sleep(1)
        print("Toma:\nGitHub: https://github.com/dlordmdia/Practicas_Python/blob/main/dlordrap_quiz.py \nYoutube Rap: https://www.youtube.com/channel/UCdHXWPzL5MbRSDNexzbTg7w \nYoutube de Drones: https://www.youtube.com/channel/UCUa5cLjlaspHPciMtEZUgZg \n\n")


time.sleep(1)
print("Gracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")