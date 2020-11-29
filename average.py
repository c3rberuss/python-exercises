num_grades = int(input("Ingrese la cantidad de notas que desea  ingresar: "))
grades = []

for index in range(num_grades):
    grade = float(input("Ingrese la nota {0}: ".format(index+1)))
    grades.append(grade)

average = sum(grades) / num_grades
print("EL promedio de notas es: {0}".format(average))
