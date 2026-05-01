class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        # enumerate the list
        # get a hashmap with num as key and the index as value
        # loop through the list
        # calculate the diff between the num and target
        # if the diff is a key in the hashmap
        # return a list containing the value and the current index
        hmap = defaultdict(int)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hmap:
                return [hmap[diff],i]
            hmap[num] = i


        