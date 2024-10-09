from .auxiliares import inicializar_matriz, mostrar_matriz, mostrar_matriz_formateada

# 1 - Obtener existencias: para ello deberá crear una función que cargue la existencia de
#     cada smartphone en todos los depósitos.
def pp_obtener_existencias(matriz: list[list]) -> None:
    inicializar_matriz(matriz)
    mostrar_matriz(matriz)
    
def mostrar_lista (matriz:list[list]):
    inicializar_matriz(matriz)
    mostrar_matriz_formateada(matriz)


