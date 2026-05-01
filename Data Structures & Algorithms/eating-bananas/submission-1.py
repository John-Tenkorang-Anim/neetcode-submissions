class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        speed = r
        while l <= r:
            k = (r + l)//2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/k)
            
            if totalTime <= h:
                speed = k
                r = k - 1
            else:
                l = k + 1
        return speed