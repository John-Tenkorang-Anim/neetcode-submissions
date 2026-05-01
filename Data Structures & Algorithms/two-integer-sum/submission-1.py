class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff not in hmap:
                hmap[num] = i
            else:
                return [hmap[diff], i]
        