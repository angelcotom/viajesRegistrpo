def registrar_clientes(n, clientes):
    if n == 0:
        return clientes

    codigo = input("Ingrese el código del cliente (ej: CL001): ")
    nombre = input("Ingrese el nombre del cliente: ")

    destinos=[]
    while True:
        destino = input(f"Ingrese un destino turistio para {nombre} (mínimo 1, máximo 5): ")
        destinos.append(destino)
        if len(destinos) == 5:
            break
        otro = input("¿Desea ingresar otro destino? (s/n): ").lower()
        if otro != 's' and len(destinos) >= 1:
            break

    clientes[codigo] = {
        "nombre": nombre,
        "destinos": destinos
    }

    return registrar_clientes(n - 1, clientes)
