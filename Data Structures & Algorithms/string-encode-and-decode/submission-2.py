class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string_count = len(s)
            string += str(string_count) + "#" + s
    
        return string

    def decode(self, s: str) -> List[str]:
        string_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            str_length = int(s[i:j])
    
            string = s[j + 1: j + 1 + str_length]
            string_list.append(string)

            i = j + str_length + 1

        return string_list
