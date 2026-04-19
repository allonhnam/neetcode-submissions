class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                # Pop two operands and add
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # Pop in reverse order: second - first
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                # Pop two operands and multiply
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                # Pop in reverse order: second / first
                a, b = stack.pop(), stack.pop()
                # Division should truncate toward zero
                stack.append(int(float(b) / a))
            else:
                # It's a number; push to stack
                stack.append(int(c))

        return stack[0]  # Final result on top of the stack
