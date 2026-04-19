class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]

        n = len(nums)
        res = [1] * n
        # [1, 1, 1, 1]

        prev = 1
        for i in range(n):
            res[i] = prev
            prev *= nums[i]
        # [1,1,2,8] 
        
        post = 1
        for i in range(n - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res

        # [48,24,12,8]