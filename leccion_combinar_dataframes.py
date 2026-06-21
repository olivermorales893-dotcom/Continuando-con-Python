import pandas as pd

# Tabla de empleados
df_empleados = pd.DataFrame({
    "id_empleado": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "María", "Carlos"],
    "id_depto": [10, 20, 10, 30]
})

# Tabla de departamentos
df_deptos = pd.DataFrame({
    "id_depto": [10, 20, 40],
    "departamento": ["TI", "Ventas", "Marketing"]
})
df_empleado = pd.merge(df_empleados, df_deptos, on="id_depto", how="inner")
print(df_empleado)

df_empleado = pd.merge(df_empleados, df_deptos, on="id_depto", how="left")
print(df_empleado)