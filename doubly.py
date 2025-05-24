class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def addstart(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def addend(self,data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def addatpos(self, pos, data):
        
        new_node = Node(data)
        len = 0
        temp = self.head
        while temp.next is not None:
            len = len + 1
            temp = temp.next
        
        if pos > len :
            
            print("Position out of range")
            return
        if pos < len:
            current = self.head 
            
        
        for i in range (pos - 1):
            current = current.next
             
        temp = current.next 
       
        current.next = new_node
        new_node.next = temp
        
             




    
    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


s = DoublyLinkedList()
s.addstart(10)
s.addstart(20)
s.addend(30)
s.addend(40)
s.addend(50)
s.addatpos(2,100)
s.display()
