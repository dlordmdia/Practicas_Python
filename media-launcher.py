# Imports
import time
import webbrowser
decidido = False
# Intro
print("\n----MEDIA LAUNCHER----\n\nQUE ES?\n Es un Launcher para abrir las Redes Sociales! \n\nPORQUE USARLO?\n Estalvias tiempo y puedes conseguir recomendaciones de cada único tipo de Red Social!\n")

# Inicio
time.sleep(2)

# Seleccionar Red Social

while not decidido:
    respuesta1 = input("Que Red Social quieres abrir?:\ntype h for help\n-")

    if respuesta1 == "h":
        print("Redes disponibles:\ni) Instagram\ny) Youtube\nt) Tik Tok\ng) GitHub\ns) Spotify\nm) Mavic Pilots\n\nr) Recomendaciones\ne) Exit Media Launcher\n\n")
    elif respuesta1 == "i":
        print("Red Social: Instagram\n Redirigiendo...")
        webbrowser.open("https://www.instagram.com/") 
    elif respuesta1 == "y":
        print("Red Social: YouTube\n Redirigiendo...")
        webbrowser.open("https://www.youtube.com")
    elif respuesta1 == "t":
        print("Red Social: Tik Tok\n Redirigiendo...")
        webbrowser.open("https://www.tiktok.com")
    elif respuesta1 == "g":
        print("Red Social: GitHub\n Redirigiendo...")
        webbrowser.open("https://www.github.com")
    elif respuesta1 == "s":
        print("Red Social: Spotify\n Redirigiendo...")
        webbrowser.open("https://www.spotify.com")
    elif respuesta1 == "m":
        print("Red Social: Mavic Pilots\n Redirigiendo...\n")
        webbrowser.open("https://www.mavicpilots.com")
    elif respuesta1 == "r":
        recs = input("Quieres Recomendaciones de unos perfiles buenos?(y/n) \n-")
    elif respuesta1 == "e":
        print("Hasta aquí el Media Launcher por ahora...\nCreado por DlordMDia ")
        exit()
        
    if respuesta1 != "h":
        decidido = True

# Recomendaciones
if recs == "y":
    while not decidido:
        recperf = input("De qué Red Social quieres un perfil?\nType -h for help")

    if respuesta1 == "h":
        print("Redes disponibles:\ni) Instagram\ny) Youtube\nt) Tik Tok\ng) GitHub\ns) Spotify\nm) Mavic Pilots\n\nr) Recomendaciones\ne) Exit Media Launcher\n\n")
    
    elif respuesta1 == "i":
        insta = input("Red Social: Instagram\n Que quieres ver?\na) Perfiles de dron\nb)Perfiles de Música")
        if insta == "a":
            webbrowser.open("https://www.instagram.com/drone.yl")
        elif insta == "b":
            webbrowser.open("https://www.instagram.com/dlord_rap")
        
    elif respuesta1 == "y":
        yt = input("Red Social: YouTube\n Que quieres ver?\na) Múltiples perfiles de Dron\nb) Perfiles de Rap")
        if yt == "a":
            webbrowser.open("https://www.youtube.com/channel/UCiqY3ffR4i_a3aJj8L4Owew")
            webbrowser.open("https://www.youtube.com/channel/UCUa5cLjlaspHPciMtEZUgZg")
        elif yt == "b":
            webbrowser.open("https://www.youtube.com/channel/UCdHXWPzL5MbRSDNexzbTg7w")
            webbrowser.open("https://www.youtube.com/c/YarostheLaunchpadder")
    
    elif respuesta1 == "t":
        tt = input("Red Social: Tik Tok\n Qué quieres ver?\na) Perfil de Rap\nb)Perfil de Dron")
        if tt == "a":
            webbrowser.open("https://www.tiktok.com/@dlord_rap")
        elif tt == "b":
            webbrowser.open("https://www.tiktok.com/@dlordair")
    
    elif respuesta1 == "g":
        print("Red Social: GitHub\n Redirigiendo...")
        webbrowser.open("https://www.github.com")
    elif respuesta1 == "s":
        print("Red Social: Spotify\n Redirigiendo...")
        webbrowser.open("https://www.spotify.com")
    elif respuesta1 == "m":
        print("Red Social: Mavic Pilots\n Redirigiendo...\n")
        webbrowser.open("https://www.mavicpilots.com")
    elif respuesta1 == "r":
        recs = input("Quieres Recomendaciones de unos perfiles buenos?(y/n) \n-")
    elif respuesta1 == "e":
        print("Hasta aquí el Media Launcher por ahora...\nCreado por DlordMDia ")
        exit()

    if respuesta1 != "h":
        decidido = True


elif recs == "n":
    print("Hasta aquí el Media Launcher por ahora...\nCreado por DlordMDia ")
    exit()
    
# Fin
print("Hasta aquí el Media Launcher por ahora...\nCreado por DlordMDia ")

