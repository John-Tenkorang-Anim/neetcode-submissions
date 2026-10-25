class Solution:
    def isValid(self, s: str) -> bool:

        hmap = {"(":")", "{":"}", "[":"]"}
        stack = []

        for char in s:
            if char in hmap:
                stack.append(char)
            else:
                if not stack or char != hmap[stack[-1]]:
                    return False

                stack.pop()    
        
        return len(stack) == 0
        