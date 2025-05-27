from funciones import (menu,
                       cargar_pacientes,
                       mostrar_pacientes,
                       buscar_paciente,
                       ordenar_matriz,
                       mostrar_mayor,
                       mostrar_menor,
                       contar_pacientes,
                       promedio_internacion)

from validaciones import (matriz_vacia,
                          cantidad_pacientes,
                          buscado,
                          opcion_valida)

opcion = 0
FILTRO = 5

pacientes = []

while opcion != 9:

    menu()

    opcion = input("Elija la opción deseada: ")
    
    if matriz_vacia(pacientes) and opcion != "1":
        print ("La lista se encuentra vacía, por favor primero ingrese datos. (Opción 1).")
        continue

    if opcion_valida(opcion):
        opcion = int(opcion)

        match opcion:
            case 1:
                cantidad = cantidad_pacientes()
                cargar_pacientes(pacientes, cantidad)
            
            case 2:
                mostrar_pacientes(pacientes)
            
            case 3:
                historia_clinica = buscado()
                buscar_paciente(pacientes, historia_clinica)
            
            case 4:
                ordenar_matriz(pacientes)

            case 5:
                mostrar_mayor(pacientes)

            case 6:
                mostrar_menor(pacientes)

            case 7:
                pacientes_contados = contar_pacientes(pacientes, FILTRO)
                print(f"Hay {pacientes_contados} pacientes con más de {FILTRO} días de internación.")

            case 8:
                promedio = promedio_internacion(pacientes)
                print(f"El promedio de días de internación es de {promedio}.")

            case 9:
                print("Gracias por usar nuestro servicio. Saliendo del programa.")
    else:
        print("Por favor ingrese una opción valida.")

print("Programa finalizado.")