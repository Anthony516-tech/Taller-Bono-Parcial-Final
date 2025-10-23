# Importamos a la clase padre:
from Node import Node
from DoubleLinkedList import DoubleLinkedList
lista_clientes = DoubleLinkedList()

# Creamos la clase del cliente:
class Costumer(Node):
    def __init__(self, name, lastname, phone, isActive):
        self.name = name
        self.lastname = lastname 
        self.phone = phone
        self.isActive = isActive
        self.id = lista_clientes._size + 1
        self.data = {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "phone": self.phone,
            "isActive": self.isActive
        }
    

    # Hacemos la funcionalidad de agregar un nuevo cliente:
    def registrar_cliente(self):
        lista_clientes.prepend(self)

    
    # Hacemos la funcionalidad de listar clientes:
    def listar_clientes():
        lista_clientes.traverse()


