import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)  # Ensures truncation towards zero
        }
        
            stack = []
        
            for token in tokens:
                if token in ops:  # If token is an operator
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(ops[token](a, b))
                else:  # If token is a number
                    stack.append(int(token))
        
            return stack[0]
        