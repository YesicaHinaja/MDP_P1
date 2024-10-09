
def mostrar_listas_formateada (matriz_data_heroes: list[list]):
    """_summary_ recibe una matriz con datos y muestra las listas en formato planilla de modo que sea mas legible.

    Args:
        matriz (list): matriz de listas a mostrar
    """
    
    cantidad_columnas = len(matriz_data_heroes[0])
    cantidad_filas = len(matriz_data_heroes)
    for indice in range(cantidad_columnas):
        texto = ""
        for sub_indice in range(cantidad_filas):
            
            if type(matriz_data_heroes[sub_indice][indice]) == str:
                
                if len(matriz_data_heroes[sub_indice][indice]) >= 7:
                    texto_original = matriz_data_heroes[sub_indice][indice]
                    texto_saneado = texto_original[:10]
                    texto += f"{texto_saneado:2} | "
                else:
                    texto += f"{matriz_data_heroes[sub_indice][indice]:7} | "
                
            elif type(matriz_data_heroes[sub_indice][indice]) == int:
                texto += f"{matriz_data_heroes[sub_indice][indice]:03} | "
                
            elif type(matriz_data_heroes[sub_indice][indice]) == float:
                texto += f"{matriz_data_heroes[sub_indice][indice]:8.2f} | "
                
            else:
                texto += f"{matriz_data_heroes[sub_indice][indice]} | "
                
                
        texto = texto[0 : -3]
        print(texto)


def sumar_filas (matriz: list[list], fila: int)-> int:
    suma = 0
    for columna in matriz[fila]:
        suma += matriz[columna]
    return suma

def obtener_marcas(matriz)->list[str]:
    marcas = []
    for marca in matriz[0]:
        if not marca in marcas:
            marcas.append(marca)
    return marcas


def obtener_menos_unidades_totales(matriz: list[list]):
    lista_marcas = []
    indice_menor_cantidad = None
    for indice in range(len(matriz[1])):
        if menor_cantidad == None or matriz[1][indice_menor_cantidad] < menor_cantidad:
            indice_menor_cantidad = indice

    marca = matriz[0][indice_menor]
    cantidad = matriz[1][indice_menor]
    texto = f"la marcar que menos unidades tiene es  {marca} con {cantidad}"
