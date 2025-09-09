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
    #Crear las subopciones de filtrar
    print("3. Ordenar países")
    print("4. Mostrar estadísticas")
    print("5. Salir")

# Función principal
def main():
    # Cargar los datos de países
    ruta_archivo = 'countries.csv'
    lista_de_paises = cargar_paises(ruta_archivo)

    opcion = 0
    # Bucle para mostrar el menú y procesar las opciones
    while opcion == 0:
        menu()
        opcion = int(input("Seleccione una opción (1-5): "))

        # Opciones del menú
        if opcion == 1:
            # Pedimos al usuario el país a buscar
            pais_usuario = input("Ingrese el nombre del país a buscar: ")
            resultado = buscar_pais(pais_usuario, lista_de_paises)

            if resultado: # Si lo encontramos, mostramos sus datos
                print("País encontrado:", resultado["nombre"])
                print("Población:", resultado["poblacion"])
                print("Superficie:", resultado["superficie"])
                print("Continente:", resultado["continente"])
            else: 
                print("País no encontrado.")
        if opcion == 2:
            print("1. filtar por continente")
            print("2. filtrar por Rango de población")
            print("3. filtrar por Rango de superficie")
            opcion = int(input("Seleccione una opción (1-3): "))

            if opcion == 1:
                continente_usuario = input("Ingrese el continente a filtrar: ")
                print("Países en el continente", continente_usuario, ":")
                if continente_usuario:
                    for pais in lista_de_paises:
                        if pais["continente"].lower() == continente_usuario.lower():
                            print("-", pais["nombre"])
            elif opcion == 2:
                poblacion_min = int(input("Ingrese la población mínima: "))
                poblacion_max = int(input("Ingrese la población máxima: "))
                print("Países con población entre", poblacion_min, "y", poblacion_max, ":")
                for pais in lista_de_paises:
                    if poblacion_min <= int(pais["poblacion"]) <= poblacion_max:
                        print("-", pais["nombre"])
            elif opcion == 3:
                superficie_min = int(input("Ingrese la superficie mínima: "))
                superficie_max = int(input("Ingrese la superficie máxima: "))
                print("Países con superficie entre", superficie_min, "y", superficie_max, ":")
                for pais in lista_de_paises:
                    if superficie_min <= int(pais["superficie"]) <= superficie_max:
                        print("-", pais["nombre"])
            
        elif opcion == 5:
            print("Muchas gracias, hasta luego!")
            break

main() 






