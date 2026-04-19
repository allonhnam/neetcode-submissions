import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)  # Count the frequency of each number

        for key, val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))        # Push (frequency, number)
            else:
                heapq.heappushpop(heap, (val, key))     # If heap is full, pushpop (min-heap keeps k most frequent)
        
        return [h[1] for h in heap]  # Extract just the numbers from the heap
