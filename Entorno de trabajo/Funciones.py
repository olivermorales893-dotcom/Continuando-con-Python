# FUNCIÓN 1: Saluda a una persona por su nombre
def saludar(nombre):
    print("¡Hola,", nombre, "!")

saludar("Oliver")  # Llama a la función con el nombre "Oliver"

# FUNCIÓN 2: Suma dos números y devuelve el resultado
def sumar(a, b):
    return a + b  # Devuelve la suma para usarla después

resultado = sumar(5, 3)  # Guarda el resultado de sumar 5 + 3
print("El resultado de la suma es:", resultado)  # Imprime: 8

# FUNCIÓN 3: Dice si una persona es mayor o menor de edad
def esmayoredad(edad):
    if edad >= 18:
        print("Eres mayor de edad")  # Si tiene 18 o más
    else:
        print("Eres menor de edad")  # Si tiene menos de 18

esmayoredad(27)  # Llama a la función con la edad 27