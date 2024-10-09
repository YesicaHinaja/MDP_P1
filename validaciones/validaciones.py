def validar_opcion (num_min: int, num_max: int)->int:
        print ("2 entro a validar")
        opcion = input(f"Ingrese una opcion entre {num_min} y {num_max}: ")
        if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max):
                return (validar_opcion(num_min, num_max))
        else: return int(opcion)

