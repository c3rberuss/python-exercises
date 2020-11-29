valid_answers = ("s", "S", "si", "Si", "SI", "sI")
conversion_factors = (
    ("Ingrese la cantidad de Libras que desea convertir a Kilos: ", 0.454545454),
    ("Ingrese la cantidad de Kilos que desea convertir a Libras: ", 2.2),
    ("Ingrese la cantidad de Euros que desea convertir a Dólares: ", 1.20),
    ("Ingrese la cantidad de Dólares que desea convertir a Euros: ", 0.84),
)

menu = """
    [ ¿QUÉ DESEA CONVERTIR? ]
    
    [ 1 ] - Libras a Kilos
    [ 2 ] - Kilos a Libras
    [ 3 ] - Euros a Dólares
    [ 4 ] - Dólares a Euros
    
    [ 5 ] - Salir
    
    [ * ] : """

while True:
    answer = int(input(menu))

    if 0 < answer < 5:
        value_to_convert = float(input(conversion_factors[answer-1][0]))
        result = value_to_convert * conversion_factors[answer-1][1]

        print("El resultado de su conversión es: {}".format(result))

        try_again = input("¿Desea realizar otra conversión? [s/n]: ")
        if try_again not in valid_answers:
            break
    elif answer == 0:
        continue
    else:
        break
