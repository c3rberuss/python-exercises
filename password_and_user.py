valid_answers = ["s", "S", "si", "Si", "SI", "sI"]
password = "$PassWord!20#"

print("***                      BIENVENIDO                      ***")
print("*** Para ingresar al sistema debe ingresar su contraseña ***\n")

while True:
    user_password = input("Ingrese la contraseña: ")

    if user_password == password:
        print("¡Bienvedido!")
        break
    else:
        print("¡Vaya!, Su contraseña es incorrecta.")
        try_again = input("¿Desea intentar nuevamente? [s/n]: ")

        if try_again not in valid_answers:
            print("¡Adiós!")
            break