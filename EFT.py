def cupos_genero(genero, peliculas, cartelera):

    total = 0

    for codigo in peliculas:

        if peliculas[codigo][1].lower() == genero.lower():
            total += cartelera[codigo][1]

    print("Total de cupos disponibles:", total)


def busqueda_precio(p_min, p_max, peliculas, cartelera):

    lista = []

    for codigo in cartelera:

        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]

        if precio >= p_min and precio <= p_max and cupos > 0:

            titulo = peliculas[codigo][0]
            lista.append(titulo + "--" + codigo)

    lista.sort()

    if len(lista) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print(lista)


peliculas = {
    "P101": ["Luz de Otoño", "drama", 110, "B", "Español", False],
    "P102": ["Noche Neón", "acción", 125, "C", "Ingles", True],
    "P103": ["Planeta Agua", "documental", 90, "A", "Español", False],
    "P104": ["Risa Total", "comedia", 105, "A", "Español", True],
    "P105": ["Código Zero", "thriller", 118, "C", "Ingles", True],
    "P106": ["Viaje Lunar", "ciencia ficción", 132, "B", "Ingles", False]
}

cartelera = {
    "P101": [5990, 40],
    "P102": [7990, 0],
    "P103": [4990, 25],
    "P104": [6990, 12],
    "P105": [8990, 8],
    "P106": [7490, 3]
}
def buscar_codigo(codigo, peliculas):

    codigo = codigo.upper()

    for cod in peliculas:

        if cod.upper() == codigo:
            return cod

    return None


def actualizar_precio(codigo, nuevo_precio, peliculas, cartelera):

    codigo_encontrado = buscar_codigo(codigo, peliculas)

    if codigo_encontrado == None:
        return False

        cartelera[codigo_encontrado][0] = nuevo_precio

        return True

    elif opcion == 3:

        seguir = "s"

    while seguir.lower() == "s":

        codigo = input("Ingrese código de la película: ")

        while True:

            try:

                nuevo_precio = int(input("Ingrese nuevo precio: "))

                if nuevo_precio > 0:
                    break

                else:
                    print("El precio debe ser mayor que 0")

            except:

                print("Debe ingresar un número entero")

        if actualizar_precio(codigo, nuevo_precio, peliculas, cartelera):
            print("Precio actualizado")
        else:
            print("El código no existe")

        seguir = input("¿Desea actualizar otro precio (s/n)?: ")
def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    return True


def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True


def validar_genero(genero):
    if genero.strip() == "":
        return False
    return True


def validar_duracion(duracion):
    if duracion > 0:
        return True
    return False


def validar_clasificacion(clasificacion):
    clasificacion = clasificacion.upper()

    if clasificacion == "A" or clasificacion == "B" or clasificacion == "C":
        return True

    return False


def validar_idioma(idioma):
    if idioma.strip() == "":
        return False
    return True


def validar_3d(es_3d):
    es_3d = es_3d.lower()

    if es_3d == "s" or es_3d == "n":
        return True

    return False


def validar_precio(precio):
    if precio > 0:
        return True
    return False


def validar_cupos(cupos):
    if cupos >= 0:
        return True
    return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):

    codigo = codigo.upper()

    if codigo in peliculas:
        

        if es_3d.lower() == "s":
            es_3d = True
        else:
            es_3d = False

            peliculas[codigo] = [titulo, genero, duracion, clasificacion.upper(), idioma, es_3d]
            cartelera[codigo] = [precio, cupos]

            return True
    elif opcion == 4:
        while True:
            try:
                duracion = int(input("Ingrese duración: "))
                precio = int(input("Ingrese precio: "))
                cupos = int(input("Ingrese cupos: "))
            except:
                print("Debe ingresar valores enteros")
                continue

    clasificacion = input("Ingrese clasificación: ")
    idioma = input("Ingrese idioma: ")
    es_3d = input("¿Es 3D? (s/n): ")

    if not validar_codigo(codigo):
        print("Código inválido")

    elif not validar_titulo(titulo):
        print("Título inválido")

    elif not validar_genero(genero):
        print("Género inválido")

    elif not validar_duracion(duracion):
        print("Duración inválida")

    elif not validar_clasificacion(clasificacion):
        print("Clasificación inválida")

    elif not validar_idioma(idioma):
        print("Idioma inválido")

    elif not validar_3d(es_3d):
        print("Valor de 3D inválido")

    elif not validar_precio(precio):
        print("Precio inválido")

    elif not validar_cupos(cupos):
        print("Cupos inválidos")

    else:

        if agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
            print("Película agregada")
        else:
            print("El código ya existe")

def eliminar_pelicula(codigo, peliculas, cartelera):

    codigo_encontrado = buscar_codigo(codigo, peliculas)

    if codigo_encontrado == None:
        return False

    del peliculas[codigo_encontrado]
    del cartelera[codigo_encontrado]

    return True


def mostrar_menu():

    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")


def leer_opcion():

    while True:

        try:

            opcion = int(input("Ingrese opción: "))

            if opcion >= 1 and opcion <= 6:
                return opcion

            print("Debe seleccionar una opción válida")

        except:

            print("Debe seleccionar una opción válida")


def main():

    while True:

        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:

            genero = input("Ingrese género: ")
            cupos_genero(genero, peliculas, cartelera)

        elif opcion == 2:

            while True:

                try:

                    minimo = int(input("Ingrese precio mínimo: "))
                    maximo = int(input("Ingrese precio máximo: "))

                    if minimo >= 0 and maximo >= minimo:
                        break

                    print("Debe ingresar un rango válido")

                except:

                    print("Debe ingresar valores enteros")

            busqueda_precio(minimo, maximo, peliculas, cartelera)

        elif opcion == 3:

            seguir = "s"

            while seguir.lower() == "s":

                codigo = input("Ingrese código de la película: ")

                while True:

                    try:

                        nuevo_precio = int(input("Ingrese nuevo precio: "))

                        if nuevo_precio > 0:
                            break

                        print("Precio inválido")

                    except:

                        print("Debe ingresar valores enteros")

                if actualizar_precio(codigo, nuevo_precio, peliculas, cartelera):
                    print("Precio actualizado")
                else:
                    print("El código no existe")

                seguir = input("¿Desea actualizar otro precio (s/n)?: ")

        elif opcion == 4:

            codigo = input("Ingrese código: ")
            titulo = input("Ingrese título: ")
            genero = input("Ingrese género: ")

            try:

                duracion = int(input("Ingrese duración: "))
                precio = int(input("Ingrese precio: "))
                cupos = int(input("Ingrese cupos: "))

            except:

                print("Debe ingresar valores enteros")
                continue

            clasificacion = input("Ingrese clasificación: ")
            idioma = input("Ingrese idioma: ")
            es_3d = input("¿Es 3D? (s/n): ")

            if not validar_codigo(codigo):
                print("Código inválido")

            elif not validar_titulo(titulo):
                print("Título inválido")

            elif not validar_genero(genero):
                print("Género inválido")

            elif not validar_duracion(duracion):
                print("Duración inválida")

            elif not validar_clasificacion(clasificacion):
                print("Clasificación inválida")

            elif not validar_idioma(idioma):
                print("Idioma inválido")

            elif not validar_3d(es_3d):
                print("Valor 3D inválido")

            elif not validar_precio(precio):
                print("Precio inválido")

            elif not validar_cupos(cupos):
                print("Cupos inválidos")

            else:

                if agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
                    print("Película agregada")
                else:
                    print("El código ya existe")

        elif opcion == 5:

            codigo = input("Ingrese código de la película: ")

            if eliminar_pelicula(codigo, peliculas, cartelera):
                print("Película eliminada")
            else:
                print("El código no existe")

        elif opcion == 6:

            print("Programa finalizado.")
            break


main()