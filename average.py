num_grades = input("Ingrese la cantidad de notas que desea  ingresar: ")
num_grades = int(num_grades)
grades = []

for index in range(num_grades):
    grade = input("Ingrese la nota {0}: ".format(index+1))
    grades.append(int(grade))

average = sum(grades) / num_grades
print("EL promedio de notas es: {0}".format(average))
