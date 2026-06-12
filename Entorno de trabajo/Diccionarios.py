miinformacion = {"nombre": "Oliver", "edad": 27, "ciudad": "querétaro", "hobby": "jugar_CODM"}  # Crea el diccionario con 4 datos

print(miinformacion["nombre"])   # Imprime: Oliver
print(miinformacion["edad"])     # Imprime: 27
print(miinformacion["ciudad"])   # Imprime: querétaro
print(miinformacion["hobby"])    # Imprime: jugar_CODM

miinformacion["correo"] = "olivermorales@gmail.com"  # Agrega el dato "correo" al diccionario
print(miinformacion["correo"])   # Imprime: olivermorales@gmail.com

del miinformacion["ciudad"]      # Elimina la clave "ciudad" del diccionario
print(miinformacion)             # Imprime el diccionario completo sin "ciudad"

for clave, valor in miinformacion.items():  # Recorre todo el diccionario
    print(clave, ":", valor)                # Imprime cada clave con su valor