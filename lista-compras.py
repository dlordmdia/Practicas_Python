import time
import webbrowser
import os
seguir = "y"

lista = []
anadiendo = False

precio_total = 0.0

print("\nQue quieres hacer?\n")
time.sleep(2)
menu1 = "\na) Añadir cosas\nb) Ver lista\nc) Ver código mientras tu compra\nd) Añadir Precios\ne) Ver precio Total\nf) Eliminar Objeto de la lista\ng) Eliminar Precio\n\nPresiona /ENTER\ para salir de la lista de compras"

print(menu1)

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
                print(menu1)

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
            print(menu1)

    elif inicio == "c":
        os.system('cls' if os.name=='nt' else 'clear')
        print("Redirigiendote a GitHub...")
        time.sleep(1)
        webbrowser.open("https://github.com/dlordmdia")
        time.sleep(3)
        os.system('cls' if os.name=='nt' else 'clear')
        print(menu1)

    elif inicio == "d":
        os.system('cls' if os.name=='nt' else 'clear')
        calculando = True
        while calculando:
            precio = input("-x to Leave | Un precio: ")
            if precio == "x":
                print("Saliendo...")
                calculando = False
                os.system('cls' if os.name=='nt' else 'clear')
                print(menu1)

            else:
                precio_total += float(precio)

    elif inicio == "e":
        os.system('cls' if os.name=='nt' else 'clear')
        xleave = input(f"Tu precio total és: {precio_total}€\n\n -x to Leave:\n- ")
        if xleave == "x":
            os.system('cls' if os.name=='nt' else 'clear')
            print(menu1)

    elif inicio == "f":
        anadiendo = True
        os.system('cls' if os.name=='nt' else 'clear')
        print("\n-x to Leave | Que Objeto quieres eliminar de la lista?")
        while anadiendo:
            print("Tienes: ")
            for item in lista:
                print(f"- {item}")

            item_to_remove = input("\nEliminas: ")
            if item_to_remove == "x":
                os.system('cls' if os.name=='nt' else 'clear')
                print(menu1)
                anadiendo = False
            
            else:
                if item_to_remove in lista:
                    for item in lista:
                        if item == item_to_remove:
                            lista.pop(lista.index(item_to_remove))
                    print("Eliminado!!\n")
                
                else:
                    print("Este objeto no está en la lista\n")

    else:
        print("\nGracias por usar la lista de compras de dlordmdia!\n\n")
        time.sleep(3)
        print("Redirigiendote a GitHub (@dlordmdia)...")
        time.sleep(1)
        webbrowser.open("https://github.com/dlordmdia")
        time.sleep(2)
        print("Abierto correctamente!\n")
        break