
def contar_destinos(lista_codigos, clientes, i):
    if i == len(lista_codigos):
        return 0
    return contar_destinos(lista_codigos, clientes, i + 1) + len(clientes[lista_codigos[i]]["destinos"])

# encontrar al cliente con más destinos
def cliente_con_mas_destinos(clientes):
    mayor = ""
    cantidad_mayor = 0
    for datos in clientes.values():
        cantidad = len(datos["destinos"])
        if cantidad > cantidad_mayor:
            cantidad_mayor = cantidad
            mayor = datos["nombre"]
    return mayor, cantidad_mayor

# P
clientes = {}
n = int(input("¿Cuántos clientes desea ingresar? "))

for i in range(n):
    print(f"\nCliente #{i + 1}")
    codigo = input("Ingrese el código del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")

    while True:
        cantidad = int(input("¿Cuántos destinos desea registrar? (1 a 5): "))
        if 1 <= cantidad <= 5:
            break
        print("Debe ingresar entre 1 y 5 destinos.")

    destinos = []
    for j in range(cantidad):
        destino = input(f"Destino {j + 1}: ")
        destinos.append(destino)

    clientes[codigo] = {"nombre": nombre, "destinos": destinos}

# Muestra resultado
print("\n=== LISTADO DE CLIENTES Y DESTINOS VISITADOS ===")
for codigo, datos in clientes.items():
    print(f"\nCódigo: {codigo}")
    print(f"Nombre: {datos['nombre']}")
    print("Destinos:", ", ".join(datos["destinos"]))

# Total de destino
codigos = list(clientes.keys())
total = contar_destinos(codigos, clientes, 0)


nombre_mayor, cantidad = cliente_con_mas_destinos(clientes)

print(f"\nTotal de destinos registrados entre todos los clientes: {total}")
print(f"Cliente con más destinos: {nombre_mayor} ({cantidad} destinos)")
