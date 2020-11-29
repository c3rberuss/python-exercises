def time_converter(time: float):
    minutes = time - int(time)
    minutes = minutes * 60
    seconds = int(minutes - int(minutes))
    minutes = int(minutes)
    hours = int(time)

    def plural(value):
        return "s" if value > 1 else ""

    parts = []

    if hours > 0:
        parts.append("{0} hora{1}".format(hours, plural(hours)))

    if minutes > 0:
        parts.append("{0} minuto{1}".format(minutes, plural(minutes)))

    if seconds > 0:
        parts.append("{0} segundo{1}".format(seconds, plural(seconds)))

    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return parts[0] + " y "+parts[1]

    return parts[0] + ", "+parts[1]+" y "+parts[2]


distance = input("Ingrese la distancia que recorrerá (Km): ")
speed = input("Ingrese la velocidad a la que viajará (Km/h): ")

total_time = float(distance) / float(speed)
total_time = time_converter(total_time)

result_str = "El tiempo que demorará en recorrer {0} Km a una velocidad constante de {1} Km/h es de {2}"

print(result_str.format(distance, speed, total_time))
