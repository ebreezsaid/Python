class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    
    def enqueue(self,item):
        self.items.append(item)
        
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty, cannot pop any item")
        
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("stack is empty, cannot peek any item")
        
     def size(self):
        return len(self.items)
   
            


            