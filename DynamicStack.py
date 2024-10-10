class Stack: # Dynamic Stack
    def __init__(self): 
        self.stack = []
        
    def print_stack(self): 
        for x in reversed(self.stack): print(f"|{x}|") 
        
    def push(self, element): 
        self.stack.append(element) 
        
    def pop(self): 
        if not self.stack:
            return print("Error: Stack Underflow, stack is empty.")
        self.stack.pop()
        
    def peek(self): 
        return print(self.stack[len(self.stack)-1])
    
    def is_empty(self):
        if not self.stack: return True
        else: return False
    
stack = Stack()
print("Pop when empty: ")
stack.pop()

print(f"\nIs empty: {stack.is_empty()}")

print("\nPushing values 1,2,3,4,5: ")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.print_stack()

print(f"\nIs empty: {stack.is_empty()}")

print(f"\nPeek:")
stack.peek()

print("\nPop: ")
stack.pop()
stack.print_stack()