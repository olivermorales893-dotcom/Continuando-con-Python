imprimetablamultiplicar = int(input("¿De qué número quieres la tabla de multiplicar? "))
print(f"Tabla de multiplicar del {imprimetablamultiplicar}:")
for i in range(1, 11):
    resultado = imprimetablamultiplicar * i
    print(imprimetablamultiplicar, "x", i, "=", resultado)