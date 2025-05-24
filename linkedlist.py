class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singly:
    
    def __init__(self):
        self.head = None


    def addstart(self,data):
        tmp = Node(data)
        tmp.next = self.head
        self.head = tmp


    def addend(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        
        p = self.head
        while p.next is not None :
                
            p = p.next 
                
        p.next = Node(data)

    def addatpos(self,pos,data):
        
        len = 0
        temp = self.head
        while temp.next is not None:
            len += 1
            temp = temp.next
        
        if pos > len:
            print("Invalid psoition")
            return
        if pos == 0:
            self.addstart(data)
            return
        if pos == len:
            self.addend(data)
            return
        if pos < len:
            current = self.head
            for i in range(pos-1):
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
        
    def delete(self,pos,data):
        len = 0
        temp = self.head
        while temp.next is not None:
            len += 1
            temp = temp.next
        if pos > len:
            print("Invalid psoition")
            return
        else:
            current = self.head
            for i in range(pos-1):
                current = current.next
            current.next = current.next.next


    def display(self):
        current = self.head
        while current is not None:
            print(current.data,end="-->")
            current = current.next


s = singly()
s.addstart(23)
s.addstart(24)
s.addend(25)
s.addend(26)
s.addend(27)
s.display()
s.addatpos(3,100)
print("\n after adding at position 3")
s.display()
s.delete(3,100)
print("\n after deleting at position 3")    
s.display()