class Solution:
    def validPalindrome(self, s: str) -> bool:

        l, r  = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s,l+1,r) or self.isPalindrome(s,l,r-1)

            l += 1
            r -= 1

        return True


    def isPalindrome(self, s, left, right):

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and right > left:
                right -= 1
            if s[left] != s[right]:
                return False
            right -= 1
            left += 1

        return True
        