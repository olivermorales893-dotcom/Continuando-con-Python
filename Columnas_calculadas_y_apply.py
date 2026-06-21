import pandas as pd

data = {
    "producto": ["Laptop", "Teclado", "Monitor", "Mouse"],
    "precio": [15000, 600, 4500, 300],
    "stock": [5, 15, 0, 50]
}
df = pd.DataFrame(data)
# Crear una nueva columna "valor_inventario" que sea el resultado de multiplicar "precio" por "stock"
df["valor_inventario"] = df["precio"] * df["stock"]
print(df)
# Crear una nueva función "revisardisponibilidad(stock)" que clasifique los productos según su precio
def revisardisponibilidad(stock):
    if stock == 0:
        return "Agotado"
    elif stock <= 10:
        return "Bajo"
    else: 
        return "Disponible"
    print(revisardisponibilidad(0))  # Imprime: Agotado
    print(revisardisponibilidad(5))  # Imprime: Disponible  
# Aplicar la función a la columna "stock" para crear una nueva columna "estado"
df["estado"] = df["stock"].apply(revisardisponibilidad)
print(df)