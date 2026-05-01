class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        left = 0
        n, k = len(s2), len(s1)
        res = False
        for right in range(n - k + 1):
            # opening the window
            nlist = list(s2[left:k])
            if Counter(list(s1)) == Counter(nlist):
                return not res
            else:
                left += 1
                k += 1
        return res





        