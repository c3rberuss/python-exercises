valid_answers = ("s", "S", "si", "Si", "SI", "sI")
password = "$PassWord!20#"

header = """
    ***                      BIENVENIDO                      ***
    *** Para ingresar al sistema debe ingresar su contraseña ***
    
"""
print(header)

while True:
    user_password = input("Ingrese la contraseña: ")

    if user_password == password:
        print("¡Bienvedido al Sistema!")
        break
    else:
        try_again = input("¿Contraseña incorrecta ¿desea intentarlo nuevamente? [s/n]: ")

        if try_again not in valid_answers:
            print("¡Adiós!")
            break
