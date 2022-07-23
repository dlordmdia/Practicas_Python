# Imports
import time
import webbrowser

# START

print("\n----DLORD ABOUT----\n\n QUÉ ES?\n És el código más informativo de Dlord!\n\n PARA QUE SIRVE?\n Ejecutando este código vas a ser informado a TU GUSTO PERSONAL sobre Dlord. Podrás saber cosas como: Información con sus Amigos, de donde salen las ideas e incluso puedes escuchar, mirar y guardar TODO TIPO de su contenido! Interesante, verdad?\n")
input("Presiona /-ENTER-\ para Continuar:\n")
info1 = input("____________________\n\n Que quieres saber?\n\na) Información de él y sus amigos\nb) De donde han surgido Ideas\nc) Como hace todas sus canciones con VideoClips\nd) Información de sus drones\ne) Cosas especiales\n")

if info1 == "a":
    música = input("Mientras lees la Info, quieres escuchar música de fondo? (y/n): \n- ")
    if música == "y":
        webbrowser.open("https://www.youtube.com/watch?v=R2AJOOvZgbc&list=PLNawVVX6lTrQmEqCXKAFlYEHf-fveJc22")
    else:
        print("Ok!")
    print("Él es Shamin Dlord Rap y fue nacido en Mallorca el cuál sigue siendo su lugar de residencia hoy en día. Fue nacido el día 9 de Agosto, año 2007 en el hospital de Manacor. El ahora vive en Sant llorenç de's Cardassar el cual es el municipio donde viven la mayoría de sus amigos. Un amigo suyo muy bueno con el cuál está casi cada día es Yaros, Ucraniano nacido en 2006. Vuelan drones apartado d y usan Kali-Linux y Python apartado "" el la calle.")
        