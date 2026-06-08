from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            c = str(len(i)) + "#" + i
            encode = encode + c
        return encode

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1 #stops at j=1 and runs j = j + 1  this statement if condition is true

            length = int(s[i:j]) 
            i = j + 1 #i = j + 1   # i = 2
            result.append(s[i:i + length])
            i = i + length

        return result
