from Node import Node

# Creamos la clase de la lista doble:
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
     

    def prepend(self, new_node):
        new_node.prev = None
        new_node.next = self.head

        if self.head is not None:
            new_node.prev = self.tail

        new_node.prev = None 
        self.head = new_node
        self._size += 1
    
    def traverse(self):
        current = self.head
        
        while current:
            print(current.data)
            current = current.next