import time
import webbrowser
import os
seguir = "y"

lista = []
anadiendo = False

precio_total = 0.0

print("\nQue quieres hacer?\n")
time.sleep(2)
print("\na) Añadir cosas\nb) Ver lista\nc) ¡¡Cerrar lista de compras!!\nd) Abrir Calculadora\ne) Ver precio Total")

while True:
    inicio = input("- ")
    if inicio == "a":
        anadiendo = True
        os.system('cls' if os.name=='nt' else 'clear')
        while anadiendo:
            objeto = input("-x to Leave | Tu objeto: ")
            if objeto == "x":
                print("Saliendo...")
                anadiendo = False
                os.system('cls' if os.name=='nt' else 'clear')
                print("\na) Añadir cosas\nb) Ver lista\nc) ¡¡Cerrar lista de compras!!\nd) Abrir Calculadora\ne) Ver precio Total")

            else:
                lista.append(objeto)
            
    elif inicio == "b":
        os.system('cls' if os.name=='nt' else 'clear')
        print("Tienes: ")
        for item in lista:
            print(f"- {item}")
        saleave = input("\n\n-x to Leave:\n- ")
        if saleave == "x":
            os.system('cls' if os.name=='nt' else 'clear')
            print("\na) Añadir cosas\nb) Ver lista\nc) ¡¡Cerrar lista de compras!!\nd) Abrir Calculadora\ne) Ver precio Total")
    
    elif inicio == "c":
        os.system('cls' if os.name=='nt' else 'clear')
        print("Saliendo...")
        time.sleep(1)
        print("\n\nGracias por usar Lista de Compras de @dlordmdia\n")
        exit()

    elif inicio == "d":
        os.system('cls' if os.name=='nt' else 'clear')
        calculando = True
        while calculando:
            precio = input("-x to Leave | Un precio: ")
            if precio == "x":
                print("Saliendo...")
                calculando = False
                os.system('cls' if os.name=='nt' else 'clear')
                print("\na) Añadir cosas\nb) Ver lista\nc) ¡¡Cerrar lista de compras!!\nd) Abrir Calculadora\ne) Ver precio Total")

            else:
                precio_total += float(precio)

    elif inicio == "e":
        os.system('cls' if os.name=='nt' else 'clear')
        xleave = input(f"Tu precio total és: {precio_total}€\n\n -x to Leave:\n- ")
        if xleave == "x":
            os.system('cls' if os.name=='nt' else 'clear')
            print("\na) Añadir cosas\nb) Ver lista\nc) Cerrar lista de compras!!\nd) Abrir Calculadora\ne) Ver precio Total")
