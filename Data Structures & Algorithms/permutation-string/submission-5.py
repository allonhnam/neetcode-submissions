class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        for c in s1:
            count1[c] += 1
        required = len(count1)

        for i in range(len(s2)):
            curr = 0
            count2 = defaultdict(int)

            for j in range(i, len(s2)):
                count2[s2[j]] += 1

                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    curr += 1
            
            if curr == required:
                return True
        
        return False