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

print("y) Yes\nn) No ")

respuesta1 = input("\nTu respuesta (y/n) : ")

if respuesta1.lower() == "y":
    equation = input("\nCuál es tu ecuación? ")
    print(f"Resultado: {eval(equation)}")
    time.sleep(2)

else:
    print("Acceptado\nGracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")

#saber mas sobre dlord

time.sleep(1)

print("\nQuieres saber más sobre DlordMDia?")
time.sleep(1)
print("\ny) Yes\nn) No \n")
time.sleep(1)
respuesta2 = input("\n Tu respuesta (y/n): ")

if respuesta2 == "y":
    print("Este texto aún está en construcción... Pruébalo más tarde!")

else:
    print("Gracias por usar Idiot Calculator\n--Creado por DlordMDia--\n")
