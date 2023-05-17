"""Properties"""


class Article:
    iva = 0.21
    """Re-Escribir el ejercicio anterior utilizando una property en vez de un
    método de instancia.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 property
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar métodos de instancia
        - No utilizar Dataclasses
        - Utilizar Type Hints en todos los métodos y variables
    """
def __init__(self, nombre: str, costo: float, descuento: float = 0) -> None:
    self._nombre = nombre
    self._costo = costo
    self._descuento = descuento

@property
def nombre(self) -> str:
    return self._nombre

@property
def precio(self) -> float:
    precio_sin_descuento = self._costo * (1 + self.iva)
    precio_con_descuento = precio_sin_descuento * (1 - self._descuento)
    return round(precio_con_descuento, 2)

@classmethod
def actualizar_iva(cls, nuevo_iva: float) -> None:
    cls.iva = nuevo_iva

@classmethod
def calcular_precio(cls, costo: float, descuento: float = 0) -> float:
    precio_sin_descuento = costo * (1 + cls.iva)
    precio_con_descuento = precio_sin_descuento * (1 - descuento)
    return round(precio_con_descuento, 2)

# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    article = Article()
    assert False, "No se puede instanciar sin nombre ni costo"
except TypeError:
    assert True

try:
    article = Article("Auto")
    assert False, "No se puede instanciar sin costo"
except TypeError:
    assert True

try:
    article = Article(nombre="Auto", costo=1)
    assert True
except TypeError:
    assert False, "El descuento es opcional"

try:
    article = Article(nombre="Auto", costo=1)
    article.precio = 2
    assert False, "No se puede modificar el precio"
except AttributeError:
    assert True


# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.precio == 1.21


article = Article("Auto", 1, 0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.25
# NO MODIFICAR - FIN