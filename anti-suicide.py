# imports
import time
import webbrowser
import random 

# start
print("\n----ANTI SUICIDE----\n made by @dlordmdia\n")

# Primera pregunta
preg1 = input("\nSentiendote un poco mal? (y/n): ")
if preg1 == "y":
    motiv = input("\nNo te preocupes... Yo te ayudo. Quieres una frase motivadora? (y/n): ")
    if motiv == "y":
        frases = ['Si tú sabes lo que vales, ve y consigue lo que mereces.\n', 'Por muy alta que sea una montaña, siempre hay un camino hacia la cima.\n', 'El triunfo verdadero del hombre surge de las cenizas del error.\n', 'Lo único imposible es aquello que no intentas.\n']
        random_item = random.choice(frases)
        print(random_item)
    else:
        print("Acceptado! Habrá otra forma de motivarte!\n")
elif preg1 == "n":
    print("Pues para qué ejecutas este codigo!!??\n")
else:
    print("Nada te puede salvar... Toma tu decisión. ")

#Segunda pregunta
print("Estoy aquí para ayudarte!\n")
time.sleep(2)
preg2 = input("Quieres un poco de música adecuada? (y/n): ")
if preg2 == "y":
    print("\nAbriendo YouTube en tu Browser...\n")
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=3pNpHZ1yv3I")
elif preg2 == "n":
    print("\nAcceptado! Habrá otra forma de motivarte!\n")
else:
    print("Nada te puede salvar... Toma tu decisión. ")

# Pregunta 3
print("Necesitas desahogarte?\n")
time.sleep(2)
print("Quieres hablar con álguien por Teléfono?\n")
time.sleep(2)
print("Para eso está internet!\n")
time.sleep(2)
preg3 = input("Quieres ir a la Página Web(y/n): ")
if preg3 == "y":
    print("Abriendo tu Browser...\n")
    time.sleep(1)
    webbrowser.open("https://telefonodelaesperanza.org/")
elif preg3 == "n":
    seg = input("\nSegur@? (y/n): ")
    if seg == "y":
        print("Espero que te haya podido ayudar!\nSi tienes mejoras, quejas o algúna idea contactame en GitHub")
        git = input("Quieres ir a GitHub? (y/n): ")
        if git == "y":
            print("Abriendo GitHub... ")
            time.sleep(1)
            webbrowser.open("https://github.com/dlordmdia")
            exit()
        elif git == "n":
            print("Espero haberte ayudado... ")
            exit()
    else:
        print("Abriendo tu Browser...\n")
        time.sleep(1)
        webbrowser.open("https://telefonodelaesperanza.org/")
print("Espero que te haya podido ayudar!\nSi tienes mejoras, quejas o algúna idea contactame en GitHub")
git = input("Quieres ir a GitHub? (y/n): ")
if git == "y":
    print("Abriendo GitHub... ")
    time.sleep(1)
    webbrowser.open("https://github.com/dlordmdia")
    exit()
elif git == "n":
    print("Espero haberte ayudado... ")
    exit()