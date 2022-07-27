def qmasq(a, b):
    return a + b

def qmenosq(c, d):
    return c - d

def qporq(e, f):
    return e * f

def qdividq(g, h):
    return g / h


while True:
    decisión = input("Que quieres calcular?\na) Sumas\nb) Restas\nc) Multiplicaciones\nd) Divisiones\n\n-x to Leave\n- ")
    if decisión == "a":
        numeroa = int(input("Primer número para tu suma: "))
        numerob = int(input("Segundo número para tu suma: "))

        resultado = qmasq(numeroa, numerob)

        print(resultado)

    elif decisión == "b":
        numeroc = int(input("Primer número para tu resta: "))
        numerod = int(input("Segundo número para tu resta: "))

        resultado = qmenosq(numeroc, numerod)

        print(resultado)

    elif decisión == "c":
        numeroe = int(input("Primer número para tu multiplicación: "))
        numerof = int(input("Segundo número para tu multiplicación: "))

        resultado = qporq(numeroe, numerof)

        print(resultado)

    elif decisión == "d":
        numerog = int(input("Primer número para tu división: "))
        numeroh = int(input("Segundo número para tu división: "))

        resultado = qdividq(numerog, numeroh)

        print(resultado)

    elif decisión == "x":
        break

    else:
        input("Parece que te has equivocado de opción...\n\nPulsa /ENTER\ para volver al menú.\n- ")