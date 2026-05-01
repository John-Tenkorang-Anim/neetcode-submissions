from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)
        for ch in strs:
            k = "".join(sorted(ch))
            hmap[k].append(ch)
        
        return [ v for _, v in hmap.items()]

            


        