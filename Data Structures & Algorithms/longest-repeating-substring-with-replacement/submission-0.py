class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1 #expanding the window

            #shrinking the window if the window len - max frequency is greater
            #than k ( meaning we can't do all the replacements)
            if (right - left +1) - max(count.values()) > k:
                count[s[left]] -= 1 #reducing the frequency size
                left += 1 #shifting the left pointer( reducing the window size)
            res = max(res, right -left + 1)
        return res

        
