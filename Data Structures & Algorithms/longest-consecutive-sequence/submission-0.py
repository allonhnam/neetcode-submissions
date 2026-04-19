from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  # Convert list to set for O(1) lookups
        longest = 0         # Tracks the length of the longest sequence found

        for num in numSet:
            # Only start counting if `num` is the beginning of a sequence
            # i.e., (num - 1) is not in the set, so this is the first in the chain
            if (num - 1) not in numSet:
                length = 1
                # Count how long the consecutive sequence is
                while (num + length) in numSet:
                    length += 1
                # Update the longest sequence found so far
                longest = max(length, longest)
        
        return longest  # Return the length of the longest consecutive sequence
