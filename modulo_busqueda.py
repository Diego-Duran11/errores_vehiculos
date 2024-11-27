from errores import errores_bmw 

def buscar_error(codigo_a_buscar):
    for error in errores_bmw:
        if error["codigo_error"] == codigo_a_buscar:
            return error
    return None