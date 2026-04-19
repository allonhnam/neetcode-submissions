class MinStack:
    def __init__(self):
        self.stack = []     # Main stack to store all values
        self.minStack = []  # Auxiliary stack to track current minimum at each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the smaller value between current val and last min (or val if minStack is empty)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()     # Remove top of main stack
        self.minStack.pop()  # Remove corresponding min value

    def top(self) -> int:
        return self.stack[-1]  # Return top element of main stack

    def getMin(self) -> int:
        return self.minStack[-1]  # Return current minimum (top of minStack)
