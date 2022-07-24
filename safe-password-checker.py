import time

print("\n----SAFE PASSWORD CHECKER----\n    Created by dlordmdia\n\n")
print("Necesitas almenos 8 carácteres")
while True:
    num_digits = 0
    password = input("Pon tu Contraseña: ")
    for character in password:
        if character.isdigit():
            num_digits += 1

    if len(password) >= 8 and num_digits >= 2:
        break

    else:
        print("\nTu contraseña no es segura.\n")
        time.sleep(0.4)
        print("Inténtalo otra vez.\n")

print("\nTu contraseña es segura.\n")
time.sleep(2)
print("\n----SAFE PASSWORD CHECKER----\n    Created by dlordmdia\n")