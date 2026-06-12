personas = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Línea 1: Creó una lista con 5 nombres: Alice, Bob, Charlie, David, Eve
print(personas[0])  # Imprime "Alice"
print(personas[1])  # Imprime "Bob"
print(personas[2])  # Imprime "Charlie"
print(personas[3])  # Imprime "David"
print(personas[4])  # Imprime "Eve"

# Líneas 7-8: Agregó dos nombres nuevos al final: Franki y Oliver
personas.append("Franki")
personas.append("Oliver")

# Línea 9: Contó cuántas personas hay en total y lo imprimió → 7
print(len(personas))

# Líneas 10-11: Recorrió toda la lista con un for e imprimió todos los nombres
for persona in personas:
    print(persona)