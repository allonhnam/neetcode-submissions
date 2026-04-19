import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)

        for key, freq in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, key))
            else:
                heapq.heappushpop(heap, (freq, key))
        
        return [h[1] for h in heap]