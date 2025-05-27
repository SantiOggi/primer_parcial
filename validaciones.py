def matriz_vacia(matriz:list)->bool:
    """
    La función verifica si la matriz se encuentra vacía
     y retorna el booleano correspondiente.
    """
    return matriz == []

def opcion_valida(opcion: str)-> bool:
    """
    La función valida que el dato ingresado sea un valor numérico de 1 cifra.
    """
    return opcion.isdigit() and len(opcion) == 1

def cantidad_pacientes()-> int:
    """
    La función pregunta cuántos pacientes van a ser cargados
    y chequea que el dato ingresado sea un número positivo.
    """
    cantidad = input("¿Cuántos pacientes desea cargar?: ")
    while not cantidad.isdigit():
        print("Por favor ingrese un número.")
        cantidad = input("¿Cuántos pacientes desea cargar?: ")
    return int(cantidad)

def buscado()-> int:
    """
    La función pide el número de historia clínica del paciente a buscar y verifica que sea un número.
    Luego lo retorna.
    """
    paciente_buscado = input("Ingrese el n° de historia clínica del paciente: ")
    while not paciente_buscado.isdigit():
        print("Por favor ingrese un número.")
        paciente_buscado = input("Ingrese el n° de historia clínica del paciente: ")
    return int(paciente_buscado)

def hc_valido(i: int)->int:
    """
    La función verifica que el número de historia clinica cargado sea un número positivo.
    """
    hc = input(f"Ingrese el número de historia clínica del paciente {i+1}: ")
    while not hc.isdigit():
        print("Por favor ingrese un número.")
        hc = input(f"Ingrese el número de historia clínica del paciente {i+1}: ")
    return int(hc)

def edad_valida(i: int)->int:
    """
    La función verifica que el número de edad cargado sea un número positivo.
    """
    edad = input(f"Ingrese la edad del paciente {i+1}: ")
    while not edad.isdigit():
        print("Por favor ingrese un número.")
        edad = input(f"Ingrese la edad del paciente {i+1}: ")
    return int(edad)

def internacion_valida(i: int)->int:
    """
    La función verifica que el número de días cargado sea un número positivo.
    """
    dias = input(f"Ingrese los días de internación del paciente {i+1}: ")
    while not dias.isdigit():
        print("Por favor ingrese un número.")
        dias = input(f"Ingrese los días de internación del paciente {i+1}: ")
    return int(dias)