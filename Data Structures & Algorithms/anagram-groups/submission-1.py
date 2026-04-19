class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs:
            sortedS = ''.join(sorted(str))
            result[sortedS].append(str)
        
        return list(result.values())