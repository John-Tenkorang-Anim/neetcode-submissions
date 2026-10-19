from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap  = Counter(s1)

        count = {}

        l = r = 0
        window_length = len(s1)

        while r < len(s2):

            if not s2[r] in hmap:
                r += 1
                l = r
                count.clear()
        
            else:
                while r < len(s2) and s2[r] in hmap:
                    count[s2[r]] = 1 + count.get(s2[r], 0)
                    r += 1
                
                    while r - l > window_length:
                        count[s2[l]] -= 1

                        if count[s2[l]] == 0:
                            del count[s2[l]]

                        l += 1

                    if r - l == window_length:
                        if hmap == count:
                            return True

        return False



        