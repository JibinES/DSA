class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class circular:
    def __init__(self):
        self.head = None
    
    def addstart(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node
        

    def addend(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
    
    def addpos(self,pos,data):
        new_node = Node(data)
        temp = self.head
        len = 0
        while temp.next != self.head:
            len += 1
            temp = temp.next
        if pos > len:
            print("Invalid position")
        if pos == 0:
            return self.addstart(data)
        if pos == len:
            return self.addend(data)
        if pos < len:
            current = self.head
            for i in range(pos-1):
                current = current.next
            temp = current.next
            current.next = new_node
            new_node.next = temp
    
    def delete(self,pos):
        temp = self.head
        len = 0
        while temp.next != self.head:
            len += 1
            temp = temp.next
        if pos > len:
            print("Invalid position")
        if pos == 0:
            current = self.head
            self.head = current.next
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head

            

        if pos < len:
            current = self.head
            for i in range (pos-1):
                current = current.next
            current.next = current.next.next

        




        

        

        
        


    def display(self):
        current = self.head
        elements = []
        while current is not None:
            if current.next == self.head:
                elements.append(current.data)
                break
            else:
                elements.append(current.data)
                current = current.next
        
        print("Circular linked list:", elements)
    
    
            
            
        
s = circular()
s.addstart(12)
s.addstart(13)
s.addstart(14)
s.addend(15)
s.addend(16)
s.addpos(2,100)
s.addpos(5,200)
s.delete(2)
s.delete(1)
s.display()