from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        else:
            vlist = self.hmap[key]
            n = len(vlist)

            l = 0
            r = n - 1
            ans = ""

            while l <= r:
                mid = (l + r) // 2

                if vlist[mid][0] == timestamp:
                    return vlist[mid][1]
                
                elif vlist[mid][0] < timestamp:
                    ans  = vlist[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return ans
           






        
