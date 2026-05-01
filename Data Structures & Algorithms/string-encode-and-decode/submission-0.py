class Solution:
    def __init__(self):
        self.idx = [] 
    def encode(self, strs: List[str]) -> str:
        ans = ""
        i = 0
        self.idx = []
        for char in strs:
            ans += char
            i += len(char)
            self.idx.append(i)
        return ans

    def decode(self, s: str) -> List[str]:
        lst = []
        start = 0
        for end in self.idx:
            lst.append(s[start:end])
            start = end
        return lst
