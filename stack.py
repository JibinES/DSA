class stack:
    def __init__(self):
        self.size = 5
        self.stack=[]
    
    def push(self,element):
        if len(self.stack) >= self.size:
            print('Stack overflow')
        else:
            self.stack.append(element)
            print(f"Pushed {element} into the stack")
    
    def pop(self):
        if len(self.stack) == -1:
            print("Stack underflow !")
        else:
            element = self.stack.pop()
            print(f"Popped {element} from stack")
    def peek(self):
        top_element = self.stack[-1]
        print("Top element is ",top_element)
    
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements are :",self.stack)
    
    def pop_index(self,index):
        if index < 0 or index > len(self.stack):
            print("Invalid index")
        else:
            element = self.stack.pop(index)
            print(f"popped {element} from stack")
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
s = stack()
s.push(20)
s.push(12)
s.peek()
s.display()
s.pop()
s.display()

