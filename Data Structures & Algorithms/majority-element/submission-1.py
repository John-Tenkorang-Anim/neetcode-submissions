
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        i = 0
        j = (n // 2)

        while i < n and j < n:
            if nums[i] == nums[j]:
                return nums[i]
            i += 1
            j += 1


