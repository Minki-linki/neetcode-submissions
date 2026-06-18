class Solution:

    def encode(self, strs: List[str]) -> str:
        rs = ''
        for i in strs:
            rs += str(len(i)) + '#' + i
        return rs
    def decode(self, s: str) -> List[str]:
        word = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            chisl = int(s[l:r])
            l = r + 1
            r =  chisl + l
            word.append(s[l:r])
            l = r
        return word

