from .auxiliares import inicializar_matriz, mostrar_matriz, mostrar_matriz_formateada, sumar_fila

# 1 - Obtener existencias: para ello deberá crear una función que cargue la existencia de
#     cada smartphone en todos los depósitos.
def pp_obtener_existencias(matriz: list[list]) -> None:
    inicializar_matriz(matriz)
    mostrar_matriz(matriz)
    
def mostrar_lista (matriz:list[list]):
    inicializar_matriz(matriz)
    mostrar_matriz_formateada(matriz)

def mostrar_suma_fila(matriz: list[list], fila:int, campo_de_suma:str)->float:
    suma = sumar_fila(matriz, fila)
    mensaje = f"La cantidad total de {campo_de_suma} de {suma}"
    print(mensaje)

def obtener_menos_unidades_totales(matriz:list[list]):

    indice_menor = None
    for columna in range(len(matriz[1])):
        if indice_menor == None or matriz[1][columna] < matriz[columna][indice_menor]:
            indice_menor = columna
    
    marca = matriz[0][indice_menor]
    cantidad = matriz[1][indice_menor]
    texto = f"la marca con menos unidades tiene es {marca} con "\
            f"{cantidad} unidades y esta en el deposito nro {indice_menor+1}"
    print (texto)
            
    
    

