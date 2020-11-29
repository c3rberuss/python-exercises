print("    [ CÁLCULO DE ÍNDICE DE MASA CORPORAL ]\n")

weight = input("    Ingrese su peso en Kilogramos: ")
weight = float(weight)

height = input("    Ingrese su altura en Metros: ")
height = float(height)

IMC = weight / (height**2)

table = """
    *****************************************************************
    *  ÍNDICE DE MASA CORPORAL  *        CLASIFICACIÓN              *
    *****************************************************************      
    *       < 16.00             *  Infrapeso: Delgadez Severa       *
    *    16.00 - 16.99          *  Infrapeso: Delgadez moderada     *
    *    17.00 - 18.49          *  Infrapeso: Delgadez aceptable    *
    *    18.50 - 24.99          *  Peso Normal                      *
    *    25.00 - 29.99          *  Sobrepeso                        *  
    *    30.00 - 34.99          *  Obeso: Tipo I                    *
    *    35.00 - 40.00          *  Obeso: Tipo II                   *
    *       > 40.00             *  Obeso: Tipo III                  *
    *****************************************************************
                           
"""

print(table)
print("    Su IMC es de {}".format(IMC))
