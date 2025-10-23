# Importamos el objeto 'Costumer':
from Costumer import Costumer
from DoubleLinkedList import DoubleLinkedList

lista_clientes = DoubleLinkedList()

while True:
    print(f"Bienvenido a ventas!")
    seleccion = int(input(f"Si desea registrar un cliente digite (1) \nSi desea eliminar un cliente digite (2) \nSi desea ver la lista de clientes digite (3) \nSi desea salir digite (4)\n"))

    if seleccion == 1:
        print("A continuación ingrese los siguientes datos del nuevo cliente:")
        name = input("Nombre del cliente: ")
        lastname = input("Apellido del cliente: ")
        phone = input("Número telefónico del cliente: ")
        

        costumer = Costumer(name, lastname, phone, True)
        print("Los datos del cliente a ingresar son:\n", costumer.data)

        # Agregamos el nuevo cliente:
        costumer.registrar_cliente()
    
    elif seleccion == 2:
        print("Lista de clientes registrados: ")
        Costumer.listar_clientes()
