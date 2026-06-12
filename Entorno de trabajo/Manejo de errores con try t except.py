try:
    numero1 = int(input("Dame un número: "))
    numero2 = int(input("Dame otro número: "))
    print("La division es:", numero1 / numero2)
except ValueError:
    print("Error: Por favor, introduce números válidos.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")