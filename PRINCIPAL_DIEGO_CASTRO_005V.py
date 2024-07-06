from FUNCIONES_DIEGO_CASTRO_005V import *

bd = [
    {
        "nombre": "diego",
        "apellido": "castro",
        "correo": "diego@gmail.com",
        "ID": 1,
        "compra": [{"fecha": "2024-07-01", "monto": 1000, "puntos":10}]
    }
]

print("bienvenidos regritro clientes todo ahorro")

while True:
    menu()

    opcion = input("opciones a ejecutar: ")

    

    if opcion == "1":
        registrar_clientes(bd)

    elif opcion == "2":
        listar_clientes(bd) 

    elif opcion =="3":
        registrar_compra(bd)


    elif opcion == "4":
        listar_puntos(bd)


    elif opcion == "5" :
        print("gracios por preferir todo ahorro")
        pass 






















