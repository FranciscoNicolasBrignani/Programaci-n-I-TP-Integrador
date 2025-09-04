import csv

# Función que carga los datos de países desde un archivo CSV
def cargar_paises(ruta):
    paises = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            pais = {
                "nombre": fila['nombre'],
                "poblacion": fila['poblacion'],
                "superficie": fila['superficie'],
                "continente": fila['continente']
            }
            paises.append(pais)
    return paises


# Función para buscar un país por nombre
def buscar_pais(pais_usuario, lista_de_paises):
    for pais in lista_de_paises:
        if pais_usuario.lower() in pais["nombre"].lower():
            return pais
    return False

# Función para mostrar el menú de opciones
def menu():
    print("----------------------------------")
    print("Menú de opciones:")
    print("1. Buscar país")
    print("2. Filtrar países")
    print("3. Ordenar países")
    print("4. Mostrar estadísticas")
    print("5. Salir")

# Función principal
def main():
    # Cargar los datos de países
    ruta_archivo = 'countries.csv'
    lista_de_paises = cargar_paises(ruta_archivo)

    # Bucle para mostrar el menú y procesar las opciones
    while True:
        menu()
        opcion = input("Seleccione una opción (1-5): ")

        # Opciones del menú
        if opcion == "1":
            # Pedimos al usuario el país a buscar
            pais_usuario = input("Ingrese el nombre del país a buscar: ")
            resultado = buscar_pais(pais_usuario, lista_de_paises)

            if resultado: # Si lo encontramos, mostramos sus datos
                print("----------------------------------")
                print("RESULTADO DE LA BÚSQUEDA:")
                print("País encontrado:", resultado["nombre"])
                print("Población:", resultado["poblacion"])
                print("Superficie:", resultado["superficie"])
                print("Continente:", resultado["continente"])
            else: 
                print("País no encontrado.")
        # Otras opciones del menú (a implementar)
        elif opcion == "2":
            print("Funcionalidad de filtrar países no implementada aún.")
        elif opcion == "3":
            # Pedimos al usuario como lo quiere ordenar
            clave = input("Ingrese para ordenar: 1. Nombre 2. Población 3. Superficie ")

            # Validamos la clave
            while clave not in ["1", "2", "3"]:
                clave = input("Ordenamiento inválido. Ingrese 1. Nombre 2. Población 3. Superficie ")

            # Ascendente o descendente en caso de población o superficie
            if clave == "2" or clave == "3":
                orden = input("Ingrese 1. Orden ascendente 2. Orden descendente: ")

                # Validamos el orden
                while orden not in ["1", "2"]:
                    orden = input("Orden inválido. Ingrese 1. Orden ascendente 2. Orden descendente: ")
        elif opcion == "4":
            print("Funcionalidad de mostrar estadísticas no implementada aún.")
        elif opcion == "5":
            print("----------------------------------")
            print("Muchas gracias, hasta luego!")
            break
        else:
            print("----------------------------------")
            print("Opción no válida, intente de nuevo.")

main() 






