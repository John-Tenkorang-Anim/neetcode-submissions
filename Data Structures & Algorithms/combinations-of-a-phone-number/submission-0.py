class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hmap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        results = []

        def backtrack(index,path):
            if len(path) == len(digits):
                results.append("".join(path[:]))
                return 
            
            possible_letters = hmap[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
            
        backtrack(0,[])
        return results