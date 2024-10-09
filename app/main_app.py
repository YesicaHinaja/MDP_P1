from validaciones import validar_opcion
from funciones import  pp_obtener_existencias, mostrar_menu, mostrar_lista
from datos import matriz_datos
import os

def utn_existencias_app():
    while True:
        mostrar_menu()  # Muestra las opciones al usuario
        opcion = validar_opcion(1, 9)  # Valida la opción ingresada por el usuario
        match opcion:
            case 1: 
                print("Cargando existencias...")
                pp_obtener_existencias(matriz_datos)  # Llama a la función para obtener existencias
            case 2:
                mostrar_lista(matriz_datos)
            case 3:
                pass  
            case 4:
                pass 
            case 5:
                pass  
            case 6: 
                pass 
            case 7: 
                pass 
            case 8:
                pass 
            case 9:
                break 
            case _:
                print("opcion incorrecta")
        os.system('pause')
        os.system('cls')
