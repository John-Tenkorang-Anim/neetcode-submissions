class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from math import prod
        #prefix sum for the list [0,1,2,8]
        #suffix sum for the list [48,24,6,0]
        ans = []
        for i in range(len(nums)):
            pref = 1 if len(nums[:i])==0 else prod(nums[:i])
            suf = 1 if len(nums[i+1:])==0 else prod(nums[i+1:])
            ans.append(pref * suf)
        return ans



        