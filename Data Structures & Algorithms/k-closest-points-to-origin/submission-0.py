import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        hmap = {}
        for point in points:
            d = (point[0])**2 + (point[1])**2
            heap.append((d, point))

        ans = heapq.nsmallest(k, heap, lambda x:x[0])
        res = []
        for m in ans:
            res.append(m[1])
        return res
            

