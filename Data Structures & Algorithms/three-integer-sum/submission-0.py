class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            j,k = i+1, len(nums)-1
            while j < k:
                ans = a + nums[j] + nums[k]
                if ans > 0:
                    k -= 1
                elif ans < 0:
                    j += 1
                else:
                    res.append([a,nums[j],nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
        return res