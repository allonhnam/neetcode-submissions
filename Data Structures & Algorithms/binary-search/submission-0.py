class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)  # Note: right is exclusive

        while l < r:
            m = l + ((r - l) // 2)  # Midpoint to avoid overflow
            if nums[m] > target:
                r = m  # Discard right half (including nums[m])
            elif nums[m] <= target:
                l = m + 1  # Keep searching right

        # Post-processing: check if the element just before 'l' matches target
        return l - 1 if (l and nums[l - 1] == target) else -1