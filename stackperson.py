class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty, cannot pop any item")
          
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("stack is empty, cannot peek any item")
            
            
    def size(self):
        return len(self.items)
    
    
    def add_guest(stack, person):
        stack.push(person)
        print(f"{person.name}  added to list.")
        
        
    def remove_guest(stack):
        if not stack.is_empty():
            removed_person = stack.pop()
            print(f"{removed_person.name} removed from the  list.")
        else:
            print(" list is empty.")

    def get_guest_count(stack):
        count = stack.size()
        print(f"Total number of guests: {count}")

    def view_guests(stack):
        print("Guest List:")
        for person in reversed(stack.items):
            print(person.name)
