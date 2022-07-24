# Imports
import string
import random
import time
import pyperclip

print("\n----PASSWORD GENERATOR----\n   Created by dlordmdia\n\n")
time.sleep(1)

# List Generator
letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

password = ""

length = int(input("Cuantos digitos quieres que tenga tu nueva Contraseña? (Recomendado: 8+)\n- "))

for i in range(length):
    charactertype = random.randint(1, 3)
    if charactertype == 1:
        password += random.choice(letters)
    elif charactertype == 2:
        password += random.choice(digits)
    else:
        password += random.choice(symbols)

print(f"Tu contraseña es: {password}")
passcopy = input("\nCopiar contraseña a portapapeles? (y/n): ")
if passcopy == "y":
    pyperclip.copy(password)
    print("\nCopiado!\n")

time.sleep(0.5)
print("\n----PASSWORD GENERATOR----\n   Created by dlordmdia\n\n")