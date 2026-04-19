class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        # [1, 1, 1, 1]

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # [1, 1, 2, 8]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        # postfix = 48
        
        # [48,24,12,8]
            
        return res