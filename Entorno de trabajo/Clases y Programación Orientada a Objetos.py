class coche :
    def __init__(self, marca, modelo, edad):
        self.marca = marca
        self.modelo = modelo
        self.edad = edad

    def mostrar_informacion(self):
        print("Marca", self.marca, "Modelo", self.modelo, "Edad", self.edad)

coche1 = coche("Toyota", "Corolla", 2020)
coche1.mostrar_informacion()
coche2 = coche("Honda", "Civic", 2020)
coche2.mostrar_informacion()