class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += str(len(i)) + '@' + i 
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        x = 0
        while x < len(s):
            y = x
            while s[y] != '@':
                y += 1
            lit = int(s[x:y])
            x = y + 1
            y = x + lit
            res.append(s[x:y])
            x = y
                

        return res

