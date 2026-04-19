from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # key: character count tuple, value: list of anagrams

        for str in strs:
            count = [0] * 26  # Initialize frequency count for 26 letters (a-z)

            for char in str:
                # Map each character to an index and increment its count
                count[ord(char) - ord('a')] += 1

            # Use the character count tuple as a key (e.g., (1,0,0,...,1) for "ab")
            res[tuple(count)].append(str)

        # Return the grouped anagrams as a list of lists
        return list(res.values())