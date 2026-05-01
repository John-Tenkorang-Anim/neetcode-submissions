class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []

        def backtrack(nums, res, index):
            if len(nums)== index:
                stack.append(res[:])
                return
            
            res.append(nums[index])
            backtrack(nums, res, index + 1)
            
            res.pop()
            backtrack(nums, res, index + 1)

        backtrack(nums,[],0)
        return stack
        