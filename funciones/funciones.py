from data import depositos
from .auxiliares import mostrar_listas_formateada, sumar_filas
"""
def obtener_existencias(depositos:list[list]):
    mostrar_listas_formateada(depositos)

def calcular_cantidad_total_smarthphones(datos: list[list]):
    lista_marcas = datos[0]
    lista_precios = datos[1]
    lista_stock = datos[2]

    for indice in range(len(lista_marcas)):
        pass
"""

def mostrar_suma_filas(matriz: list[list], fila:int, campo_suma:str )-> float:
    suma = sumar_filas(matriz, fila)
    mensaje = f'la cantidad total de {campo_suma} es de {suma}'
    print (mensaje)


