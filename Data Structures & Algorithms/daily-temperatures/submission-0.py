class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # Initialize result list with 0s
        stack = []  # Stack to store (temperature, index) pairs

        for i, t in enumerate(temperatures):
            # If current temp is warmer than the one at the top of the stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # Record how many days until a warmer temperature
                res[stackInd] = i - stackInd
            # Push current temp and its index onto the stack
            stack.append((t, i))

        return res  # Any index left in stack has no warmer day ahead → remains 0
