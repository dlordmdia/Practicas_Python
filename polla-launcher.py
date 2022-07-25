import webbrowser
import time
import os


while True:
    dick = input("\nQuieres abrir una polla? (y/n): ")
    if dick == "y":
        webbrowser.open("https://englishlib.org/dictionary/img/wlibrary/p/60315ec15909f8.28416852.jpg")
    elif dick == "n":
        print("No me importa...")
        time.sleep(1)
        print("Abriendo...")
        time.sleep(1)
        webbrowser.open("https://englishlib.org/dictionary/img/wlibrary/p/60315ec15909f8.28416852.jpg")
    elif dick == "exit":
        print("\nComo sabías esto?\n")
        exit()
    
    else:
        print("Parece que te has equivocado... ")
    