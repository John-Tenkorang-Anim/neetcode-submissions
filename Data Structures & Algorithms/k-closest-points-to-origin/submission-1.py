import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []

        for u,v in points:
            heapq.heappush(max_heap, (-(u**2 + v**2),[u,v]))
            
            while len(max_heap) > k:
                heapq.heappop(max_heap)

        return [p for _, p in max_heap]
        