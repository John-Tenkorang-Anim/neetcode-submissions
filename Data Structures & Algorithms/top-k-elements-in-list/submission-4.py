import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)

        max_heap = []
        for n, v in hmap.items():
            max_heap.append((-v,n))
        
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]

        