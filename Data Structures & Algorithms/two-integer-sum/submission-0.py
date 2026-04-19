class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # init map
        map = {} # val -> index
        # iterate through nums enum
        for i, n in enumerate(nums):
        # diff = target - nums[i]
            diff = target - n
        # see if it exists in the map
            if diff in map:
                return [map[diff], i]
            map[n] = i
