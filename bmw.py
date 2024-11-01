errores_bmw = [
    {
        "codigo_error": "P0171",
        "descripcion": (
            "Mezcla de combustible demasiado pobre en el banco 1. Este código de error indica que el motor "
            "está recibiendo más aire que combustible, lo que provoca una mezcla pobre. Las causas comunes "
            "pueden incluir fugas en el sistema de admisión, un sensor MAF sucio o defectuoso, o problemas "
            "en los inyectores de combustible."
        ),
        "solucion": (
            "Verificar si hay fugas de vacío en las mangueras y el sistema de admisión. Limpiar o "
            "reemplazar el sensor MAF si está sucio y revisar el sistema de inyección de combustible."
        )
    },
    {
        "codigo_error": "P0300",
        "descripcion": (
            "Fallo de encendido aleatorio. Este código indica que uno o más cilindros están experimentando "
            "fallos de encendido de manera irregular, lo cual puede ser causado por bujías desgastadas, "
            "bobinas de encendido defectuosas o problemas en el suministro de combustible."
        ),
        "solucion": (
            "Revisar y reemplazar las bujías si están desgastadas, verificar las bobinas de encendido "
            "y asegurarse de que cada cilindro esté recibiendo suficiente combustible. Si el problema "
            "persiste, puede ser necesario verificar la compresión en los cilindros."
        )
    },
    {
        "codigo_error": "P0455",
        "descripcion": (
            "Fuga grande en el sistema de control de emisiones evaporativas (EVAP). Este sistema evita "
            "que los vapores de combustible se escapen a la atmósfera. Una fuga grande en este sistema "
            "puede ser debido a una tapa de tanque de combustible mal cerrada, o una fuga en las mangueras "
            "o componentes del sistema EVAP."
        ),
        "solucion": (
            "Verificar la tapa del tanque de combustible y asegurarse de que esté bien cerrada y en buen estado. "
            "Si el problema persiste, revisar las mangueras y conexiones del sistema EVAP en busca de fugas."
        )
    },
    {
        "codigo_error": "P0420",
        "descripcion": (
            "Eficiencia del catalizador por debajo del umbral en el banco 1. Esto sugiere que el convertidor "
            "catalítico no está funcionando eficientemente para reducir las emisiones. Las causas pueden incluir "
            "un convertidor catalítico dañado o sensores de oxígeno defectuosos."
        ),
        "solucion": (
            "Inspeccionar el catalizador para comprobar su estado y revisar los sensores de oxígeno. "
            "Reemplazar los sensores si están defectuosos, o el catalizador si está dañado."
        )
    },
]


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

codigo_a_buscar = input("Introduce el código de error que deseas buscar (ejemplo: P0300): ")


resultado = buscar_error(codigo_a_buscar)


if resultado:

    print("\nInformación del Error Encontrado:")
    print(f"Código de Error: {resultado['codigo_error']}")
    print(f"Descripción: {resultado['descripcion']}")
    print(f"Posible Solución: {resultado['solucion']}")
else:
   
    print("Error no encontrado en la base de datos.")
