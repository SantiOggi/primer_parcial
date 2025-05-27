from validaciones import (hc_valido,
                          edad_valida,
                          internacion_valida)

def menu()-> None:
    """
    La función imprime en terminal el menú principal.
    """
    print("""
------------------------------------------------------
              MENU PRINCIPAL "LA FUERZA"
------------------------------------------------------
1 - Cargar pacientes.
2 - Mostrar pacientes.
3 - Buscar paciente.
4 - Ordenar pacientes.
5 - Mostrar internación más larga.
6 - Mostrar internación más corta.
7 - Contar pacientes con más de 5 días de internación.
8 - Tiempo promedio de interanciones.
9 - Salir. 
------------------------------------------------------
          """)

def cargar_pacientes(matriz: list, cantidad: int)-> None:
    """
    La función recibe una matriz y una cantidad que representa los pacientes a cargar.
    Luego pide los datos ya validados y los agrega a la matriz.
    """
    for i in range(cantidad):
        historia_clinica = hc_valido(i)
        nombre = input(f"Ingrese el nombre del paciente {i+1}: ")
        edad = edad_valida(i)
        diagnostico = input(f"Ingrese el diagnóstico del paciente {i+1}: ")
        internacion = internacion_valida(i)
        matriz += [[historia_clinica, nombre, edad, diagnostico, internacion]]

def mostrar_pacientes(matriz: list)-> None:
    """
    La función recibe la matriz y la imprime ordenadamente.
    """
    print("Los pacientes cargados son:")
    for i in range(len(matriz)):
        print(matriz[i])
    print("")

def buscar_paciente(matriz: list,historia_clinica: int):
    """
    La función recorre la matriz buscando pacientes con el valor de historia clínica solicitado.
    Si encuentra coincidencia imprime los datos del paciente.
    Si no hay coincidencia lo imforma.
    """
    flag = False
    for i in range(len(matriz)):
        if matriz[i][0] == historia_clinica:
            print(matriz[i])
            flag = True
    if not flag:
        print("No hay ningún paciente cargado con ese n° de historia clínica.")

def ordenar_matriz(matriz: list)-> None:
    """
    La función aplica el ordenamiento burbuja en la matriz,
    ordenando ascendentemente los valores de la primera columna.
    """
    n = len(matriz)
    for i in range (n-1):
        for j in range(n-i-1):
            if matriz[j][0] > matriz [j+1][0]:
                aux = matriz[j]
                matriz[j] = matriz[j+1]
                matriz [j+1] = aux

def mostrar_mayor(matriz: list)-> None:
    """
    La función revisa una primera vez la matriz para buscar la internación más larga.
    Luego la vuelve a revisar para chequear si hay varios pacientes esa misma duración de internación.
    Por último los imprime en consola.
    """
    mayor = matriz[0][4]
    indices = [0]
    for i in range(1, len(matriz)):
        if matriz[i][4] > mayor:
            mayor = matriz[i][4]
            indices = [i]

    for j in range(len(matriz)):
        if matriz[j][4] == mayor and j != indices[0]:
            indices += [j]

    print("El/los paciente/s con internación más larga es/son: ")
    for k in indices:
        print(matriz[k])

def mostrar_menor(matriz: list)-> None:
    """
    La función revisa una primera vez la matriz para buscar la internación más corta.
    Luego la vuelve a revisar para chequear si hay varios pacientes esa misma duración de internación.
    Por último los imprime en consola.
    """
    menor = matriz[0][4]
    indices = [0]
    for i in range(1, len(matriz)):
        if matriz[i][4] < menor:
            menor = matriz[i][4]
            indices = [i]

    for j in range(len(matriz)):
        if matriz[j][4] == menor and j != indices[0]:
            indices += [j]

    print("El/los paciente/s con internación más corta es/son: ")
    for k in indices:
        print(matriz[k])

def contar_pacientes(matriz: list, filtro: int)-> int:
    """
    La función cuenta cuántos pacientes tienen una internación mayor al parámetro filtro.
    """
    contador = 0
    for i in range(len(matriz)):
        if matriz[i][4] > filtro:
            contador += 1
    return contador

def promedio_internacion(matriz: list)-> int:
    """
    La función calcula el promedio de días de internación de los pacientes.
    Suma el total de días y lo divide por la cantidad de pacientes.
    Retorna ese promedio.
    """
    suma = 0
    internados = len(matriz)
    for i in range(internados):
        suma += matriz[i][4]
    return suma/internados
    
