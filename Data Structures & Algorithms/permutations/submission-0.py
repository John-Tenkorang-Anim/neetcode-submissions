class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        used = [False]*len(nums)
        def backtrack(res, used):
            if len(res) == len(nums):
                stack.append(res[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    res.append(nums[i])
                    backtrack(res, used)
                    res.pop()
                    used[i] = False

        backtrack([],used)
        return stack

