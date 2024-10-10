class Stack: # Fixed Stack
    def __init__(self, size): 
        self.stack = [None for x in range(size)]
        
    def print_stack(self): 
        for x in reversed(self.stack): print(f"|{x}|") 
        
    def push(self, element):
        if self.stack[0] == None:
            self.stack.append(element)
            self.stack.pop(0) 
        else: print("Error: Stack Overflow, stack is full")
        
    def pop(self): 
        if self.stack[-1] == None:
            return print("Error: Stack Underflow, stack is empty.")
        self.stack.pop()
        
    def peek(self): 
        return print(self.stack[len(self.stack)-1])
    
    def is_empty(self):
        if self.stack[len(self.stack)-1] == None:
            return True
        else: return False

print("Making an empty stack with space for 5 elements: ")
stack = Stack(5)
stack.print_stack()

print("\nPop when empty: ")
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