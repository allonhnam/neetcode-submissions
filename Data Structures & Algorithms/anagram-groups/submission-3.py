class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        # counter
        for s in strs:
            counter = [0] * 26 # [1],[0],[1]...[1]
        # index counter
            for c in s:
                counter[ord(c) - ord("a")] += 1
            
            res[tuple(counter)].append(s)
            # (0,1), (2,1)...

        return list(res.values())

# A dict key must be hashable (immutable with a fixed hash value).

# A list is mutable. You can change its contents, so it has no stable hash. This makes lists invalid as dictionary keys.

# A tuple is immutable. Once created, its contents do not change, so Python can compute a fixed hash and use it as a dictionary key.