class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ns = ""

        i = j  = 0

        while i < len(word1) and j < len(word2):
            ns += word1[i]
            ns += word2[j]
            i += 1
            j += 1
        
        ns += word1[i:] + word2[j:]
        return ns
        