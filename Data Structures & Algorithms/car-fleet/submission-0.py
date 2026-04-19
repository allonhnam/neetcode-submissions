class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]  # Combine positions and speeds
        pair.sort(reverse=True)  # Sort cars by starting position from closest to farthest from target

        stack = []  # Stack to track arrival times of fleets

        for p, s in pair:
            time = (target - p) / s  # Time for this car to reach the target
            stack.append(time)

            # If the current car catches up to the one ahead (arrives sooner or same time), merge fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Not a new fleet; gets absorbed into the previous one

        return len(stack)  # Remaining items in stack represent distinct fleets
