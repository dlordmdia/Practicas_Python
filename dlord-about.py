# Imports
import time
import webbrowser
decidido =False

# START

print("\n----DLORD ABOUT----\n\n QUÉ ES?\n És el código más informativo de Dlord!\n\n PARA QUE SIRVE?\n Ejecutando este código vas a ser informado a TU GUSTO PERSONAL sobre Dlord. Podrás saber cosas como: Información con sus Amigos, de donde salen las ideas e incluso puedes escuchar, mirar y guardar TODO TIPO de su contenido! \n")
input("Presiona /-ENTER-\ para Continuar:\n")
música = input("Mientras lees la Info, quieres escuchar música de fondo? (y/n): \n- ")
if música == "y":
    webbrowser.open("https://www.youtube.com/watch?v=R2AJOOvZgbc&list=PLNawVVX6lTrQmEqCXKAFlYEHf-fveJc22")
else:
    print("Ok!")
info1 = input("____________________\n\n Que quieres saber?\n\na) Información de él y sus amigos\nb) De donde han surgido Ideas\nc) Como hace todas sus canciones con VideoClips\nd) Información de sus drones\ne) Cosas especiales\n")

if info1 == "a":
    print("Entrando en Amigos... \n")
    time.sleep(1)
    print("Él es Shamin 'Dlord Rap' y fue nacido en Mallorca el cuál sigue siendo su lugar de residencia hoy en día. Fue nacido el día 9 de Agosto, año 2007 en el hospital de Manacor. El ahora vive en Sant llorenç de's Cardassar el cual es el municipio donde viven la mayoría de sus amigos. Un amigo suyo muy bueno con el cuál está casi cada día es Yaros, Ucraniano nacido en 2006. Vuelan drones 'apartado d' y usan Kali-Linux y Python 'apartado ""' el la calle. Ellos también han hecho sus propios Beats para luego cantar y rapear en ellas. Otro amigo es Erik, nacido el año 2007. Shamin y Erik se conozen desde los 3 años. Se conocieron el en cole y estuvieron hasta acabar primaria juntos en una clase. Una amiga és Martina, nacida el año 2011. Los padres de Shamin y Martina se conocen desde hace mucho tiempo y ya que Martina se ha mudado a la misma Comunidad que Shamin están haciendo música y viviendo aventuras!")

elif info1 == "b":
    print("\nEntrando a Ideas... \n")
    time.sleep(1)
    ideas = input("Que curiosidades quieres saber?\na) De donde surgen los Nombres de las canciones?\nb) De donde surgen las Letras de las canciones?\nc) De donde surgen los Beats de las canciones?\nTu elección: ")



