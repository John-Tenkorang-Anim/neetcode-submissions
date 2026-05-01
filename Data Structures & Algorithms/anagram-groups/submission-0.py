class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # use a hmap
        # the key for the hmap is sorted and added to it if not in the hmap
        # the value is appended to it if it's sorted form is a key in the hmap
        # loop through the hmap and retrieve all the values in the hmap
        hmap = defaultdict(list)

        for char in strs:
            hmap["".join(sorted(char))].append(char)

        ans = []
        for key,value in hmap.items():
            ans.append(value)
        return ans

        