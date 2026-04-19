class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)

        for char in string1:
            counter1[char] += 1
        for char in string2:
            counter2[char] += 1

        return counter1 == counter2