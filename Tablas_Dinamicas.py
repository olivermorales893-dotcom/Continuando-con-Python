import pandas as pd

# Datos de ventas de una tienda
data = {
    "Mes": ["Enero", "Enero", "Febrero", "Febrero", "Enero", "Febrero"],
    "Region": ["Norte", "Sur", "Norte", "Sur", "Norte", "Sur"],
    "Ventas": [1000, 1500, 1200, 2000, 1100, 2200]
}
df = pd.DataFrame(data)

df = df.pivot_table(index="Mes", columns="Region", values="Ventas", aggfunc="sum")
print(df)

# 🎯 TU RETO:
# 1. Crea la tabla dinámica usando .pivot_table()
#    - Filas (index): "Mes"
#    - Columnas (columns): "Region"
#    - Valores (values): "Ventas"
#    - Operación (aggfunc): "sum"

# 2. Imprime el resultado con print()