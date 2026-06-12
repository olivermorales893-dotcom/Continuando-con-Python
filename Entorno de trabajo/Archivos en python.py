# Paso 1: Escribir el archivo con nombre y ciudad
with open("Notas.txt", "w") as archivo:
    archivo.write("Nombre: Oliver\n")
    archivo.write("Ciudad: Querétaro\n")

# Paso 2: Agregar el hobby
with open("Notas.txt", "a") as archivo:
    archivo.write("Hobby: jugar CODM\n")

# Paso 3: Leer e imprimir el contenido
with open("Notas.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)