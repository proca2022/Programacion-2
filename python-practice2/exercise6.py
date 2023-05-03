"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
    numeros = []
    otros = []
    for elem in lista:
        if type(elem) in (int, float):
            numeros.append(elem)
        else:
            otros.append(elem)
    return otros + numeros

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.
    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """
    numeros = [elem for elem in lista if isinstance(elem, (int, float))]
    otros = [elem for elem in lista if not isinstance(elem, (int, float))]
    return otros + numeros

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN