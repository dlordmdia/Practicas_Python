import time

print("\n----IDIOTCALCULATOR----\n\n Created by DlordMDia\n")

time.sleep(1)

equation = input("Cuál es tu ecuación? ")

print(f"Resultado: {eval(equation)}")

time.sleep(1)

#proximo Calculo 

time.sleep(1)

print("\nQuieres hacer otro cálculo?\n")

time.sleep(1)

respuesta1 = input("\nTu respuesta (y/n) : ")

if respuesta1.lower() == "y":
    equation = input("\nCuál es tu ecuación? ")
    print(f"Resultado: {eval(equation)}")
    time.sleep(2)

else:
    time.sleep(1)
    print("\nQuieres saber más sobre DlordMDia?")
    time.sleep(1)
    respuesta2 = input("\n Tu respuesta (y/n): ")

    if respuesta2 == "y":
        time.sleep(1)
        print("Dlord Rap tiene muchos perfiles con información y contenido. Te recomiendo su Quizz para saber un poco más de él. Aquí dejo el github de su python code.\n ")
        time.sleep(5)
        respuesta3 = input("\n Lo quieres? (y/n): ")
        if respuesta3 == "y":
            print("Toma: https://github.com/dlordmdia/Practicas_Python/blob/main/dlordrap_quiz.py\n")
            time.sleep(1)
            print("Gracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")
            exit()
        else:
            print("Gracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")
            exit()
    else:
        print("Gracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")

#saber mas sobre dlord

time.sleep(1)

print("\nQuieres saber más sobre DlordMDia?")
time.sleep(1)
respuesta2 = input("\n Tu respuesta (y/n) o saltar: ")

if respuesta2 == "y":
    print("\nDlord Rap tiene muchos perfiles con información y contenido. Te recomiendo su Quizz para saber un poco más de él. Aquí dejo el github de su python code.\n ")
    respuesta3 = input("\n Lo quieres? (y/n): ")
    if respuesta3 == "y":
        time.sleep(1)
        print("Toma: https://github.com/dlordmdia/Practicas_Python/blob/main/dlordrap_quiz.py\n")
        time.sleep(1)
        print("Gracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")
    else:
        print("Gracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")
else:
    print("Gracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")
