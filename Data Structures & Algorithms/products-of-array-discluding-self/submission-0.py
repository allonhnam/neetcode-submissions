class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Compute left products
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        
        # Compute right products and multiply
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res
