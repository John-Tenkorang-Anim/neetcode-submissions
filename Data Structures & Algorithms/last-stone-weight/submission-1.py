import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones] if stones else []

        heapq.heapify(heap)
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if second != first:
                heapq.heappush(heap, -(first - second))
        
        return abs(-heap[0]) if heap else 0