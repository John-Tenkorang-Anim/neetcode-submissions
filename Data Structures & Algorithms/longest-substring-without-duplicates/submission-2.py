class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window = []
        # seen = set()
        # max_sum = 0
        # for i in range(len(s)):
        #     if s[i] not in seen:
        #         seen.add(s[i])
        #         window.append(s[i])
        #         max_sum = max(max_sum,len(window))
        #     else:
        #         seen.clear()
        #         window = []
        #         seen.add(s[i])
        #         window.append(s[i])
        #     max_sum = max(max_sum,len(window))
        # return max_sum
        window = []
        max_sum = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in window:
                window.append(s[i])
                max_sum = max(max_sum,len(window))
            else:
                window = window[window.index(s[i])+1:]
                window.append(s[i])
            max_sum = max(max_sum,len(window))
        return max_sum
