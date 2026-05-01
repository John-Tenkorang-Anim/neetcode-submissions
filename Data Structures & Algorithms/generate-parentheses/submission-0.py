class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                stack.append("".join(res.copy()))
                return

            if openN < n:
                res.append("(")
                backtrack(openN + 1, closedN)
                res.pop()
            
            if closedN < openN:
                res.append(")")
                backtrack(openN, closedN + 1)
                res.pop()

        backtrack(0,0)
        return stack
        