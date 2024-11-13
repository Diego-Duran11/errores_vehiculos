# modulo_busqueda.py

from errores import errores_bmw  # Asegúrate de que errores.py está en el mismo directorio

def buscar_error(codigo_a_buscar):
    """
    Busca un error específico en la lista de errores de BMW basado en el código de error proporcionado.

    Parámetros:
    - codigo_a_buscar (str): El código del error que queremos encontrar.

    Retorna:
    - dict o None: Retorna un diccionario con el error si se encuentra, o None si no existe.
    """
    for error in errores_bmw:
        if error["codigo_error"] == codigo_a_buscar:
            return error
    return None
