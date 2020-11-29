amount = input("    Ingrese la cantidad de dinero a invertir: $")
amount = float(amount)

interest = input("    Ingrese la tasa de interés anual que el banco pagará (%): ")
interest = float(interest)

years = input("    Ingrese el número de años de la inversión a plazo: ")
years = int(years)

interest_acum = amount * (interest/100) * years
text = """
    El monto total de los intereses a recibir por la inversión de ${0} dólares, a una tasa de 
    interés anual del {1}% y a un plazo de {2} años es de ${3}
    
      CAPITAL INICIAL   = ${0}
      INTERESES         = ${3}
    -------------------------------
          CAPITAL TOTAL = ${4}
"""

print(text.format(amount, interest, years, interest_acum, interest_acum+amount))
