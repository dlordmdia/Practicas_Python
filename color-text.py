import colorama
from colorama import Fore
import string

print("----CUSTOM-TEXT----")
while True:
    color = input("Tu color:\n\na) rojo\nb) verde\nc) amarillo\nd) rosa\ne) azul\n\n-x to Exit\n-  ")
    custom = input("Tu texto: ")

    if color == "a":
        print(Fore.RED + f'{custom}')

    if color == "b":
        print(Fore.GREEN + f'{custom}')

    if color == "c":
        print(Fore.YELLOW + f'{custom}')

    if color == "d":
        print(Fore.PINK + f'{custom}')

    if color == "e":
        print(Fore.BLUE + f'{custom}')
    
    if color == "x":
        break   
