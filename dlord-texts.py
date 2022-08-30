import time
import webbrowser
import os
from tkinter import *
import tkinter.scrolledtext as st
import tkinter as tk

letra_a = '''
Tengo todo preparado y montado para jugar porque soy un viciado
Vamos a estar en línea  hora tras hora porque soy un gran viciado

Tengo todo preparado y montado para jugar porque soy un viciado
Vamos a estar en línea  hora tras hora porque soy un gran viciado
Tengo todo preparado y montado para jugar porque soy un viciado
Vamos a estar en línea  hora tras hora porque soy un gran viciado


Vamos A jugar, nos vamos a juntar nos vamos a viciar, 
nos tenemos que concentrar, para ganar
A qué jugamos, pues nos lo tenemos que pensar,
De mientras a Tetris nos podemos conectar

Vamos a Minecraft? o vamos a un shooter
No pagamos renta entonces invertimos en el rooter
El vecino no lo roba porque le hemos hackeado
Y un poco más tarde, al tetris nos hemos conectado

Tremendo valor que tiene mi setup de la semana
Yo duermo en mi silla por eso me estalvio la cama
Auriculares profesionales para estar concentrado
Cuando al tetris me haya conectado

Tengo todo preparado y montado para jugar porque soy un viciado
Vamos a estar en línea  hora tras hora porque soy un gran viciado
Tengo todo preparado y montado para jugar porque soy un viciado
Vamos a estar en línea  hora tras hora porque soy un gran viciado


Queremos estar en línea y en directo con mucha gente
Si nos aburrimos, se abre tetris de repente
Sensores profesionales están montados
igual que los servers al tetris conectados
'''
letra_b = '''Salíamos de una forma rara,
Hacíamos cosas así por la cara,
Y te contamos qué hicimos,
De qué forma nos divertimos

Salíamos de una forma rara,
Hacíamos cosas así por la cara,
Y te contamos qué hicimos,
De qué forma nos divertimos

Scrollea, Google fotos,
Tantos recuerdos hasta romper los potos,
Nos pegamos con palos de bambú ,
Cómo jugamos, así estás tú

O con palos de metal a los arbustos de mierda,
No eran robustos ni siquiera,
Pero se coló la pequeña bolita,
Por ella nos hicimos bastante pupita

Luego conducimos adentro con un coche y una gopro,
No la vimos y nos habíamos enfadado,
También por aburrimiento, De una montaña el coche lo tiramos,
Queríamos romperlo aunque no podamos

Tanto aguanta, como los patinetes,
Los tiramos contra bordillos cuando no lo esperes,
Aguanta tanto, pero sigo siendo confundí le, 
Como el Itiwitanic es sensible

Salíamos de una forma rara,
Hacíamos cosas así por la cara,
Y te contamos qué hicimos,
De qué forma nos divertimos

Salíamos de una forma rara,
Hacíamos cosas así por la cara,
Y te contamos qué hicimos,
De qué forma nos divertimos

Producimos electricidad solo con tubos,
Para qué usan todos sus estudios,
Encuentra un par de tuberias y nos encargas,
Ya verás cuánto produce y en ganar no tardas


Daban calambres, casi como el dron de mario
Se rompió volando por el barrio,
Lo tirábamos al aire y luego lo prendemos,
Así es como lo rompemos

Como las pilas, que las metimos en el agua,
Esperando a que algún efecto haga,
Nos dé calambres y nos caigamos,
Siendo como Sergio, ya empezamos,

Que le roba la botella, y teníamos que correr por ella,
Porque Sergio en el patio se la lleva,
Es el pasado al que quiero volver,
Pero dudo que se pueda hacer

Comemos palomitas pero con azúcar y sal,
Para todos menos nosotros está mal,
Con la tutora, el apodo fue Planishit,
No te lo crees pero si

Te cuento que bugeamos un PC solo con Shul ker bo xes!
Era en minecraft tocando tambien la bateria y era tremendo estrés

Salíamos de una forma rara,
Hacíamos cosas así por la cara,
Y te contamos qué hicimos,
De qué forma nos divertimos

Salíamos de una forma rara,
Hacíamos cosas así por la cara,
Y te contamos qué hicimos,
De qué forma nos divertimos
'''
letra_c = '''Queremos practicar,
Para poder ganar,
Es la competición,
Del gran millón.

Queremos practicar,
Para poder ganar,
Es la competición,
Del gran millón.

Queremos practicar,
Para poder ganar,
Es la competición,
Del gran millón.

La competición competitiva,
Para nosotros, la decisión decisiva,
No pagamos IVA porque estamos en la fila,
Para que nos den el premio, de la mejor rima.

Hay que practicar para conseguir nuestros objetivos,
Hay que imaginarse el futuro con sentido,
No imagines, aun menos alucines,
El camino es largo, mejor que ya camines

No corras, correr al futuro cansa,
A no ser la competición el la cancha,
Velocidad de una lancha al caso de la bici,
Por eso ves caminando, por el lujo o la crisis

Queremos ganar, no por la fama y el dinero,
Vienen los verdaderos a saludar primero,
Todos tienes sus bajos y sus altos,
Sobre todo en la competición de saltos

Queremos practicar,
Para poder ganar,
Es la competición,
Del gran millón.

Queremos practicar,
Para poder ganar,
Es la competición,
Del gran millón.

Es el reto y se mantiene la rivalidad,
Deja tu ego y vuelve a la realidad,
Es la normalidad tener calma en el body,
Nervios alterados, eso ya es otra story

No te hinches a drogas o medicinas,
Pregunta amablemente a tus viejitas vecinas,
Si podrian hacerte un caldito,
Es saludable y estará calentito.

TODO OTRA VEZ MENOS LAS DOS ESTROFAS “-” y añadir otro CANTAR x2'''

getback = "Volverás al menú principal al Cerrar la Ventana."

# Start

os.system('cls' if os.name=='nt' else 'clear')

print("\n--DLORD TEXTS--\n\n")

while True:
    os.system('cls' if os.name=='nt' else 'clear')
    elegir = input("De Cuál Canción quieres la Letra?\n-h for Help\n-")

    if elegir == "a" or elegir == "Hoy en Día":
        os.system('cls' if os.name=='nt' else 'clear')
        print(getback)
        root = Tk()
        text_area = st.ScrolledText(root)
        text_area.grid(column = 0, pady = 10, padx = 10)
        text_area.insert(tk.INSERT,letra_a)
        text_area.configure(state ='disabled')
        root.mainloop()
    
    elif elegir == "b" or elegir == "El Pasado":
        os.system('cls' if os.name=='nt' else 'clear')
        print(getback)
        root = Tk()
        text_area = st.ScrolledText(root)
        text_area.grid(column = 0, pady = 10, padx = 10)
        text_area.insert(tk.INSERT,letra_b)
        text_area.configure(state ='disabled')
        root.mainloop()
    
    elif elegir == "c" or elegir == "La Competición":
        os.system('cls' if os.name=='nt' else 'clear')
        print(getback)
        root = Tk()
        text_area = st.ScrolledText(root)
        text_area.grid(column = 0, pady = 10, padx = 10)
        text_area.insert(tk.INSERT,letra_c)
        text_area.configure(state ='disabled')
        root.mainloop()
    
    elif elegir == "h":
        os.system('cls' if os.name=='nt' else 'clear')
        input("OPCIONES:\nHoy en Día (Dlord Rap, Yaros) // -a\nEl Pasado (Dlord Rap) // -b\nLa Competición (Dlord Rap, Yaros) // -c\n\n//ENTER\\ to go Back\n-")
    
    elif elegir == "x":
        os.system('cls' if os.name=='nt' else 'clear')
        break
    
    elif elegir == "porno":
            print("Disfruta cacho puta :)")
            time.sleep(1)
            while True:
                os.system('cls' if os.name=='nt' else 'clear')
                webbrowser.open("https://www.pornhub.com")
                time.sleep(0.005)

    else:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Parece que has escrito algo mal.\nIntentalo Otra Vez")
        time.sleep(1)

os.system('cls' if os.name=='nt' else 'clear')
print("Gracias por usarme ;)\n")