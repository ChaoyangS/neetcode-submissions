class MinStack:

    def __init__(self):
        #maintain 2 stack, one the full, the other, just the min element
        self.minstack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            
            self.minstack.append(val)
        

    def pop(self) -> None:
        cur = self.stack.pop()
        if cur == self.minstack[-1]:
            self.minstack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
