class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                return True
        return False
        