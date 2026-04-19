class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort array to use two-pointer approach

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue  # Skip duplicates for the first number

            l, r = i + 1, len(nums) - 1  # Two pointers

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1  # Sum too big, move right pointer left
                elif threeSum < 0:
                    l += 1  # Sum too small, move left pointer right
                else:
                    res.append([a, nums[l], nums[r]])  # Found a triplet
                    l += 1
                    # Skip duplicates for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res  # Return all unique triplets that sum to 0
