import pandas as pd

data = {
    "categoria": ["Electrónica", "Ropa", "Electrónica", "Ropa", "Alimentos", "Alimentos"],
    "producto":  ["Laptop", "Camisa", "Celular", "Pantalón", "Arroz", "Leche"],
    "precio":    [15000, 350, 8000, 500, 45, 30],
    "cantidad":  [3, 10, 5, 8, 100, 80]
}
df = pd.DataFrame(data)

# 3. Ahora sí podemos agrupar sin errores
resultado = df.groupby("categoria")["precio"].agg(["sum", "mean", "max", "min"])

print(resultado)