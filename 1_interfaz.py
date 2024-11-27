from modulo_busqueda import buscar_error
def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Buscar un código de error")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            codigo_a_buscar = input("Introduce el código de error que deseas buscar (ejemplo: P0300): ")
            resultado = buscar_error(codigo_a_buscar)
            
            if resultado:
                print("\nInformación del Error Encontrado:")
                print(f"Código de Error: {resultado['codigo_error']}")
                print(f"Descripción: {resultado['descripcion']}")
                print(f"Posible Solución: {resultado['solucion']}")
            else:
                print("Error no encontrado en la base de datos.")
        
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

if __name__ == "__main__":
    main()
