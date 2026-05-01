class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {"{": "}", "[": "]", "(": ")"}
        stack = []
        
        for char in s:
            if char in hmap:  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                if not stack or hmap[stack.pop()] != char:
                    return False  # Mismatch or empty stack

        return not stack

        

            
        