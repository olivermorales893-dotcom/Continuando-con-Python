import pandas as pd

data = {
    "empleado": ["Ana", "Luis", "Ana", "Carlos", "Sofía"],
    "edad": [25, None, 25, 35, None],
    "ciudad": ["CDMX", "GDL", "CDMX", None, "MTY"]
}
df = pd.DataFrame(data)
df_limpio = df.drop_duplicates()
print("Datos sin duplicados:")
print(df_limpio)
df_limpio = df_limpio.fillna("0")
print("Datos sin valores nulos:")
print(df_limpio)