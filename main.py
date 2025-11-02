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

def guardar_paises(ruta, lista_de_paises):
    with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
        campos = ['nombre', 'poblacion', 'superficie', 'continente']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in lista_de_paises:
            escritor.writerow(pais)

# Función para agregar un nuevo país
def agregar_pais(lista_de_paises):

    nombre = input("Ingrese el nombre del país: ")
    if buscar_pais(nombre, lista_de_paises):
        print("El país ya existe en la lista.")
        return main()
    poblacion = input("Ingrese la población del país: ")
    superficie = input("Ingrese la superficie del país: ")
    continente = input("Ingrese el continente del país: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista_de_paises.append(nuevo_pais)
    guardar_paises('countries.csv', lista_de_paises)
    print(f"País {nombre} agregado exitosamente.")

#Funcion para actualizar datos de un país
def actualizar_pais(lista_de_paises):
    nombre = input("Ingrese el nombre del país a actualizar: ")
    pais = buscar_pais(nombre, lista_de_paises)

    if not pais:
        print("El país no existe en la lista.")
        return

    nueva_poblacion = input("Ingrese la nueva población del país: ")
    nueva_superficie = input("Ingrese la nueva superficie del país: ")

    pais["poblacion"] = nueva_poblacion
    pais["superficie"] = nueva_superficie

    guardar_paises('countries.csv', lista_de_paises)
    print(f"Datos del país {nombre} actualizados exitosamente.")

# Función para mostrar el menú de opciones
def menu():
    print("----------------------------------")
    print("Menú de opciones:")
    print("1. Agregar un país")
    print("2. Actualizar los datos de población y superficie de un país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")

# Función principal
def main():
    # Cargar los datos de países
    ruta_archivo = 'countries.csv'
    lista_de_paises = cargar_paises(ruta_archivo)

    opcion = 0
    # Bucle para mostrar el menú y procesar las opciones
    while opcion != 1:
        menu()
        opcion = int(input("Seleccione una opción (1-7): "))

        #AGREGAR LAS OPCIONES 1 Y 2
        if opcion == 1:
            agregar_pais(lista_de_paises)
        
        if opcion == 2:
            actualizar_pais(lista_de_paises)
        # Opciones del menú
        if opcion == 3:
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
        if opcion == 4:
            print("1. filtrar por continente")
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
            #AGREGAR LAS DEMAS OPCIONES 5 Y 6
            
        elif opcion == 7:
            print("Muchas gracias, hasta luego!")
            break

main() 






