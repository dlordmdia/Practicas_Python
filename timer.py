import time
import os

secs = int(input("De cuántos segundos quieres que sea tu Temporizador?\nCantidad de segundos: "))
os.system('cls' if os.name=='nt' else 'clear')
print("Temporizador en marcha!")
for i in range(secs+1):
    if secs > 0:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Falta: ")
        print(f"{secs}")
        secs -= 1
        time.sleep(1)

    else:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Se acabó el tiempo!!")