from validaciones import validar_opcion
from funciones import  obtener_existencias, mostrar_menu
from data import depositos
import os

def utn_existencias_app():
    while True:
        mostrar_menu()  # Muestra las opciones al usuario
        opcion = validar_opcion(1, 9)  # Valida la opción ingresada por el usuario
        match opcion:
            case 1: 
                print("Cargando existencias...")
                obtener_existencias(depositos)  # Llama a la función para obtener existencias
            case 2:
                pass  
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
