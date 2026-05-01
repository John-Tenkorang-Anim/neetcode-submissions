class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        def backtrack(res, index):
            results.append(res[:])
            
            for i in range(index, len(nums)):

                if i > index and nums[i] == nums[i-1]:
                    continue

                res.append(nums[i])
                backtrack(res, i + 1)
                res.pop()
            
                
        backtrack([],0)
        return results
