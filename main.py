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

#Funcion para guardar los datos actualizados en el archivo CSV
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
    if nombre == "":
        print("Error: El nombre del país no puede estar vacío.")
        return main()
    if buscar_pais(nombre, lista_de_paises):
        print("El país ya existe en la lista.")
        return main()
    poblacion = input("Ingrese la población del país: ")
    if str(poblacion) == "" or poblacion == "0":
        print("Error: La población del país no puede estar vacía ni ser 0.")
        return main()
    superficie = input("Ingrese la superficie del país: ")
    if str(superficie) == "" or superficie == "0":
        print("Error: La superficie del país no puede estar vacía ni ser 0.")
        return main()
    continente = input("Ingrese el continente del país: ")
    if continente == "":
        print("Error: El continente del país no puede estar vacío.")
        return main()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    lista_de_paises.append(nuevo_pais)
    guardar_paises('countries.csv', lista_de_paises)
    print(f"País {nombre} agregado exitosamente.")
    return main()

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

        if opcion == 1:
            agregar_pais(lista_de_paises)
        
        if opcion == 2:
            actualizar_pais(lista_de_paises)
        if opcion == 3:
            pais_usuario = input("Ingrese el nombre del país a buscar: ")
            resultado = buscar_pais(pais_usuario, lista_de_paises)

            if resultado: 
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
        if opcion == 5:
            print("1. Ordenar por nombre")
            print("2. Ordenar por población")
            print("3. Ordenar por superficie")
            opcion = int(input("Seleccione una opción (1-3): "))

            if opcion == 1:
                paises_ordenados = sorted(lista_de_paises, key=lambda x: x["nombre"])
                for pais in paises_ordenados:
                    print("-", pais["nombre"])
            elif opcion == 2:
                paises_ordenados = sorted(lista_de_paises, key=lambda x: x["poblacion"])
                for pais in paises_ordenados:
                    print("-", pais["poblacion"], pais["nombre"])
            elif opcion == 3:
                paises_ordenados = sorted(lista_de_paises, key=lambda x: x["superficie"])
                for pais in paises_ordenados:
                    print("-", pais["superficie"], pais["nombre"])
            print("Países ordenados:")
            
            
        if opcion == 6:
            print("Elija las estadísticas que desea ver:")
            print("1. País con mayor y menor población")
            print("2. Promedio de población")
            print("3. Promedio de superficie")
            print("4. Cantidad de países por continente ")
            opcion = int(input("Seleccione una opción (1-4): "))

            if opcion == 1:
                pais_mayor_poblacion = max(lista_de_paises, key=lambda x: int(x["poblacion"]))
                pais_menor_poblacion = min(lista_de_paises, key=lambda x: int(x["poblacion"]))
                print("País con mayor población:", pais_mayor_poblacion["nombre"], "con", pais_mayor_poblacion["poblacion"])
                print("País con menor población:", pais_menor_poblacion["nombre"], "con", pais_menor_poblacion["poblacion"])
            elif opcion == 2:
                total_poblacion = sum(int(pais["poblacion"]) for pais in lista_de_paises)
                promedio_poblacion = total_poblacion / len(lista_de_paises)
                print(f"Promedio de población: {promedio_poblacion:.2f}")
            elif opcion == 3:
                total_superficie = sum(int(pais["superficie"]) for pais in lista_de_paises)
                promedio_superficie = total_superficie / len(lista_de_paises)
                print(f"Promedio de superficie: {promedio_superficie:.2f}")
            elif opcion == 4:
                continentes = {}
                for pais in lista_de_paises:
                    continente = pais["continente"]
                    if continente in continentes:
                        continentes[continente] += 1
                    else:
                        continentes[continente] = 1
                print("Cantidad de países por continente:")
                for continente, cantidad in continentes.items():
                    print(continente + ":", cantidad)

        elif opcion == 7:
            print("Muchas gracias, hasta luego!")
            break

main() 






