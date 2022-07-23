# imports
import time
import webbrowser
import random 

# start
print("\n----ANTI SUICIDE----\n made by @dlordmdia\n")

# Primera pregunta
preg1 = input("Sentiendote un podo mal? (y/n): ")
if preg1 == "y":
    motiv = input("No te preocupes... Yo te ayudo. Quieres una frase motivadora? (y/n): ")
    if motiv == "y":
        frases = ['Si tú sabes lo que vales, ve y consigue lo que mereces.', 'Por muy alta que sea una montaña, siempre hay un camino hacia la cima.', 'El triunfo verdadero del hombre surge de las cenizas del error.', 'Lo único imposible es aquello que no intentas.']
        random_item = random.choice(frases)
        print(random_item)
    else:
        print("Acceptado! Habrá otra forma de motivarte!")
elif preg1 == "n":
    print("Pues para qué ejecutas este codigo!!??")
else:
    print("Nada te puede salvar... Toma tu decisión. ")

#Segunda pregunta
preg2 = input("Quieres un poco de música adecuada?")