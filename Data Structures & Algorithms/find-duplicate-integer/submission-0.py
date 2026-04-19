class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # Phase 1: Find intersection point inside the cycle
        while True:
            slow = nums[slow]             # Move one step
            fast = nums[nums[fast]]       # Move two steps
            if slow == fast:
                break

        # Phase 2: Find entrance to the cycle (duplicate)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow