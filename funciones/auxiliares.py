#INICIALIZAR LA MATRIZ
import random as rd

def inicializar_matriz(matriz: list[list]) -> list[list]:
    
    posibles_marcas = [
        "Xiaomi", "Nubia", "Inifix", "Samsung"
    ]
    
    cantidad_columnas = len(matriz[0])
    
    if cantidad_columnas == 0:
        for i in range(20):
            
            # Marca
            marca_elegida = rd.choice(posibles_marcas)
            matriz[0].append(marca_elegida)
            # Cantidad
            cantidad_elegida = rd.randint(10000, 60000)
            matriz[1].append(cantidad_elegida)
            # Precio
            precio_unitario = rd.randint(150000, 1200000) + (rd.randint(10, 100) / 100)
            matriz[2].append(precio_unitario)
            # Ganancias
            ganancias = matriz[1][i] * matriz[2][i]
            matriz[3].append(ganancias)
            # Deposito inicial (Para ver la columna del deposito luego de ordenarlos por algun valor)
            deposito = i+1
            matriz[4].append(deposito)
    
    return matriz


def mostrar_dato(matriz: list[list], indice_columna: int) -> None:
    dato = f'| {(indice_columna):13} | {matriz[4][indice_columna]:8} | {matriz[0][indice_columna]:10} | {matriz[1][indice_columna]:8} | '\
            f'${matriz[2][indice_columna]:11.2f} | ${matriz[3][indice_columna]:15.2f} |'
    print(dato)
def generar_encabezado_separador(encabezado: str) -> str:
    new_line = '\n'
    separador = ''
    for _ in range(len(encabezado)):
        separador += '-'
    return f'{encabezado}{new_line}{separador}'

def mostrar_matriz(matriz: list[list]) -> None:
    cantidad_columnas = len(matriz[0])
    encabezado = '| Indice Actual | Deposito |    Marca   | Cantidad | Precio Unit  |     Ganancias    |'
    encabezado = generar_encabezado_separador(encabezado)
    print(encabezado)
    for columna in range(cantidad_columnas):
        mostrar_dato(matriz, columna)

######### fin de las funciones q no son mias a

def mostrar_matriz_formateada(matriz):
    cant_filas = len(matriz)
    cant_columnas = len(matriz[0])
    encabezado = "MARCA          |CANTIDAD       |PRECIO UNITARIO |GANANCIA        |indice        "
    linea = ("-"*15)*5
    print (linea)
    print (encabezado)
    print (linea)
    for columas in range(cant_columnas):
        texto = ""
        for filas in range(cant_filas):
            if type(matriz[filas][columas]) == str:
                texto += f"{matriz[filas][columas]:15}|"
            if type (matriz[filas][columas]) == float:
                texto += f"{matriz[filas][columas]:15.2f} |"
            if type(matriz[filas][columas]) == int:
                texto += f"{matriz[filas][columas]:15d}|"
        print (texto)
