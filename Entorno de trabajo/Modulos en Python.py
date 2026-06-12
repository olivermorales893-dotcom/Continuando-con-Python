import datetime
import random
from math import sqrt

# Fecha de hoy
hoy = datetime.date.today()
print("La fecha de hoy es:", hoy)

# 3 números aleatorios y su raíz cuadrada
for i in range(3):
    numero = random.randint(1, 100)
    print("Número aleatorio:", numero, "- Raíz cuadrada:", sqrt(numero))
