class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)  # Frequency map for characters in s1
        for c in s1:
            count1[c] += 1

        need = len(count1)  # Number of unique characters needed to match

        # Try every starting index i in s2
        for i in range(len(s2)):
            count2 = defaultdict(int)
            cur = 0  # count2 = window freq map, cur = matched character types

            for j in range(i, len(s2)):  # Expand window from i to j
                count2[s2[j]] +=1

                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break

                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1

                if cur == need:
                    return True

        return False  # No valid permutation found
