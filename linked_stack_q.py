class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_queue:
    def __init__(self):
        self.rear = None
        self.front = None
    
    def enqueue(self,data):
        new_node = Node(data)
        if (self.front == None):
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def  dequeue(self):
        if self.front == None:
            print("Underflow")
        else:
            temp = self.front
            self.front = self.front.next
            print("Element dequed = ",temp.data)
    def display(self):
        temp = self.front
        while temp:
            print(temp.data,end="--")
            temp = temp.next



s = linked_queue()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.display()
s.dequeue()
s.display()

class linked_stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            last = self.top 
            while last.next:
                last = last.next
            last.next = new_node
    
    def pop(self):
        if self.top is None:
            print("Stack underflow")
        else:
            second_last = last = self.top
            while second_last.next.next is not None:
                second_last = second_last.next
            while last.next is not None:
                last = last.next
            
            second_last.next = None
            print("\n popped element is ", last.data)
    def display(self):
        current = self.top
        while current:
            print(current.data,end="-->")
            current = current.next

j = linked_stack()
print("Stack operations")
j.push(200)
j.push(300)
j.push(400)
j.display()
j.pop()
j.display()            