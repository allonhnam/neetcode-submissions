class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Two pointers: left and right

        while l < r:
            curSum = numbers[l] + numbers[r]  # Current sum of two numbers

            if curSum > target:
                r -= 1  # Sum too big, move right pointer left
            elif curSum < target:
                l += 1  # Sum too small, move left pointer right
            else:
                return [l + 1, r + 1]  # Found the pair (1-indexed)

        return []  # No valid pair found
