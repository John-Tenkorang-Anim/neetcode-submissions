class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        hmap = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: b * a,
            "/": lambda a, b: int(a / b)
        }

        stack = [] 

        for token in tokens:
            if token not in hmap:
                stack.append(int(token))
            else:
                if stack:
                    right = stack.pop()
                    left = stack.pop()
                    
                    ans = hmap[token](left, right)
                    stack.append(ans)

        return stack[0]