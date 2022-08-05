import time
import webbrowser
import os

os.system('cls' if os.name=='nt' else 'clear')
print("\n--SIMPLE CALCULATOR--\n Creado por @dlordmdia\n\n")
print("Iniciando Sistema...")
time.sleep(1)
os.system('cls' if os.name=='nt' else 'clear')
print("TUS CÁLCULOS:\n")

while True:
    help = ("\nFormas de Calcular:\n Sumas = +\n Restas = -\n Multiplicaciónes = *\n Divisiones = /\n\n- Se pueden mezclar tipos de cálculos\n- No se guardan los Cálculos al abrir el menú de Ayuda tras hacer cálculos\n\nOtros:\n Presiona -g para abrir el GitHub del creador\n Presiona -c para ver el código de esta calculadora\n Presiona -x para salir\n\npresiona ENTER para volver a los Cálculos\n- ")
    time.sleep(0.2)
    equation = input("\n-x para salir | -h para ayuda | Ecuación: ")

    if equation == "x":
        os.system('cls' if os.name=='nt' else 'clear')
        print("gracias por usar:\n\n--SIMPLE CALCULATOR--\n\nby @dlordmdia\n")
        break

    elif equation == "h":
        os.system('cls' if os.name=='nt' else 'clear')
        helpy = input(help)
        os.system('cls' if os.name=='nt' else 'clear')
        if helpy == "g":
            print("Abriendo...")
            time.sleep(1)
            webbrowser.open("https://github.com/dlordmdia")
            os.system('cls' if os.name=='nt' else 'clear')
            print("TUS CÁLCULOS:\n")
            
    elif equation == "g":
        print("Abriendo...")
        time.sleep(1)
        webbrowser.open("https://github.com/dlordmdia")
        os.system('cls' if os.name=='nt' else 'clear')
    
    elif equation == "c":
        os.system('cls' if os.name=='nt' else 'clear')
        print("Aún no está publicada en el perfil de GitHub del Creador pero aquí esta su Perfil: ")
        time.sleep(2)
        print("Abriendo...")
        time.sleep(0.5)
        webbrowser.open("https://github.com/dlordmdia")
        os.system('cls' if os.name=='nt' else 'clear')

    else:
        print(f"Resultado: {eval(equation)}\n")
