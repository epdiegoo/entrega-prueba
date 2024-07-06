def saludos (): 
    print("sistema de registro")

def menu ():
    opciones = [
        "Registrar Cliente",
    "Listar Clientes Registrados",
    "Registrar Compra",
    "Listar Compras de un Cliente",
    "Salir programa",
    ]
    
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

def registrar_clientes(bd):
    nombre = input("Ingrese nombre del cliente: ").upper()
    apellido = input("Ingrese apellido del cliente: ").upper()
    correo = input("ingrese correo de contacto: ").upper()

    id_cliente = len(bd) + 1

    bd.append(
        {
            "nombre": nombre,
            "apellido": apellido,
            "ID": id_cliente,
            "correo": correo,
            "compra": []
        }
    )

    print("\nSE HA REGISTRADO UN CLIENTE NUEVO A LA LISTA!\n")



def lista_clientes(bd):
    print("\nLos clientes registrados son:\n")
    print("ID\t\tNOMBRE\t\tCORREO")
    for cliente in bd:
        print(f'{cliente["ID"]}\t\t{cliente["nombre"]} {cliente["apellido"]}\t\t{cliente["correo"]}')

    print("\nListado creado con éxito!\n")



def registrar_compra(bd):
    id = int(input("Ingrese el ID del cliente: "))

    for cliente in bd:
        if cliente["ID"] == id:
            fecha = input("Ingrese fecha de compra (AAAA-MM-DD): ")
            monto = int(input("Ingrese total de la compra: "))
            cliente["cpmpra"].append(
                {
                    "fecha": fecha,
                    "monto": monto,
                    "puntos": round(monto*0.01)
                }
            )
            print(f'\nSe ha agregado una compra: {cliente["nombre"]} {cliente["apellido"]}.')

            

def lista_puntos(bd):
    id = int(input("Ingrese el ID del cliente: "))

    for cliente in bd:
        if cliente["ID"] == id:
            texto = f"ID Socio: {id}\n"
            texto += f'NOMBRE CLIENTE: {cliente["nombre"]} {cliente["apellido"]}\n'
            texto += f"Fecha de compra\t\tTotal de compra\n"

            puntos_totales = 0
            for monto in cliente["compra"]:
                texto += f"{monto["fecha"]}\t\t{monto["monto"]}\t\t{monto["puntos"]}\n"
                puntos_totales += (monto["monto"])*0.01

            texto += f'puntos acumulados totales: {round(puntos_totales)} pesos'

            with open(f"resumun_cliente_id_{id}.txt", "w", encoding='utf-8') as archivo:
	            archivo.write(texto)

            print("ARCHIVO CREADO")

            break