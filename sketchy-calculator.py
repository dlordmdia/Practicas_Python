import time
import webbrowser

print("\n----SKETCHYCALCULATOR----\n\n  Created by DlordMDia")

#Empezando Cálculo

equation = input("\nCuál es tu ecuación? ")
time.sleep(1)
print("Calculando...")
time.sleep(3)
print("Esto es una ecuación difícil... ")
time.sleep(3)
for i in range(8):
    time.sleep(0.2)
    print("ERROR")
time.sleep(0.8)
print("\n\n!!FORMATEANDO DISCOS DUROS!!")
time.sleep(2)
for i in range(101):
    print(f"Proceso: {i}%")
    if i == 99:
        time.sleep(3)

    else:
        time.sleep(0.07)

print("Formatting Completed!\n")
time.sleep(1)

#Cálculo incorrecto
print(f"Resultado de la ecuación: {eval(equation) + 2}\n")
time.sleep(2)
print("ERROR 469: Ordenador Sobrecalentado\n")
time.sleep(2)
#Cálculo Correcto

calc2 = input("Repetimos el cálculo? (y/n): ")

if calc2 == "y":
    print("Calculando...\n")
    time.sleep(1)
    print(f"Resultado correcto de la ecuación: {eval(equation)}\n")
elif calc2 == "n":
    print("Como que no?? Aquí lo tienes:\n")
    time.sleep(2)
    print(f"Resultado correcto de la ecuación: {eval(equation)}\n")
else:
    time.sleep(2)
    print("Te crees my listo, eh? Toma Respuesta:")
    time.sleep(1)
    print(f"Resultado correcto de la ecuación: {eval(equation)}\n")

time.sleep(2)
print("Sentimos las molestias... Toma música motivadora!\n")
time.sleep(3)

# Opening Web Browser
webbrowser.open("https://www.youtube.com/watch?v=QuDFvn6pL4o")

# Despedida
print("Gracias por usar Sketchy Calculator\n--Creado por DlordMDia--\n")