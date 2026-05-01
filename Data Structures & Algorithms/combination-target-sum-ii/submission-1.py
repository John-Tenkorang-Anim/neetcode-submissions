class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        seen = set()
        def backtrack(start,res, total):
            if total == target:
                signature = tuple(sorted(res[:]))
                if signature not in seen:
                    seen.add(signature)
                    stack.append(res[:])
                    return
            
            if total > target:
                return

            for i in range(start, len(candidates)):
                res.append(candidates[i])
                backtrack(i+1,res,total + candidates[i])
                res.pop()

        backtrack(0,[],0)
        return stack

