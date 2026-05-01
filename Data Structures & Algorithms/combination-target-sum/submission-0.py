class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack = []

        def backtrack(start, res, total):
            if total == target:
                stack.append(res[:])
                return
            
            if total > target:
                return

            for i in range(start, len(nums)):
                res.append(nums[i])
                backtrack(i,res,total + nums[i])
                res.pop()
        backtrack(0,[],0)
        return stack