class Queue:
    def __init__(self,max_size):
        self.MAX = max_size
        self.queue = [None] * self.MAX
        self.front = -1
        self.rear = -1
    
    def isFull(self):
        return self.rear == self.MAX - 1
    def isEmpty(self):
        return self.front == -1 and self.rear == -1
    
    def enqueue(self,value):
        if self.isFull():
            print("Overflow")
        else:
            if self.front == -1:
                self.front =  0 
            self.rear += 1
            self.queue[self.rear] = value 
            print(f'Enqueued: {value}')

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty , Underflow")
        else:
            x = self.queue[self.front]
            print(f"Dequeued: {x}")
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front +=1
            return x
    def display(self):
        if self.isEmpty():
            print("Underflow")
        else:
            print("Queue content:",end=" ")
            for i in range(self.front,self.rear + 1):
                print(self.queue[i],end=" ")
            print()

q = Queue(4)
q.display()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.dequeue()
q.dequeue()
q.display()