"""
Se desea crear un programa que simule el funcionamiento basico de un vehiculo.


-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
-Crear su constructor
-Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
-crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
-Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.


Colocar abajo la comisión y nro de grupo, ademas de los integrantes del grupo ( Nombre y apellido , legajo ).A la hora de hacer el PR colocar nro de grupo y comisión en el titulo del mismo.
Comisión : X
Grupo : X
Integrantes:
-Legajo XXXX,....
-Legajo YYYY,....
.
.
.
"""

class Vehiculo:
    def __init__(self, marca, ruedas, color, en_marcha=False):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.en_marcha = en_marcha

    def arrancar(self):
        self.en_marcha = True
        print("El vehículo ha sido puesto en marcha.")
mi_auto = Vehiculo("Ford", 4, "Rojo")
mi_auto.arrancar()  # Llamada al método arrancar()

def tipoVehiculo(self):
        if self.ruedas == 4:
            return "Automóvil"
        elif self.ruedas == 2:
            return "Motocicleta"
        else:
            return "Desconocido"
def mostrar(self):
        print(f"Marca: {self.marca}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Color: {self.color}")
        print(f"En marcha: {'Sí' if self.en_marcha else 'No'}") 