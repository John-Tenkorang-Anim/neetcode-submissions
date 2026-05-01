class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []

        def backtrack(i, res):
            if i >= len(s):
                results.append(res[:])
                return

            for j in range(i, len(s)):
                if isPalindrome(s,i,j):
                    res.append(s[i:j+1])
                    backtrack(j+1,res)
                    res.pop()
        backtrack(0,[])
        return results

def isPalindrome(s,l,r):
    while l < r:
        if s[l] != s[r]:
            return False
        l,r = l+1, r-1
    return True