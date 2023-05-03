"""Bloque IF, operadores lógicos, función max y operador ternario."""


"""Toma dos números y devuelve el mayor.
Restricciones:
- Utilizar IF
- No utilizar ELSE
- No utilizar la función max
"""
def maximo_basico(a: float, b: float) -> float:
    if a > b:
        return a
    if b > a:
        return b

# NO MODIFICAR - INICIO
assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN
print(maximo_basico(10, 5)) # Output: 10
print(maximo_basico(9, 18)) # Output: 18
###############################################################################


def maximo_libreria(a: float, b: float) -> float:
    """Re-escribir utilizando el built-in max.
    Referencia: https://docs.python.org/3/library/functions.html#max
    """
    return max(a, b)

# NO MODIFICAR - INICIO
assert maximo_libreria(10, 5) == 10
assert maximo_libreria(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_ternario(a: float, b: float) -> float:
    """Re-escribir utilizando el operador ternario.
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """

    return a if a > b else b
# NO MODIFICAR - INICIO
assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN