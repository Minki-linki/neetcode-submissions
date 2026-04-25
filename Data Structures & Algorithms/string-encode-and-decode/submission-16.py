class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += str(len(i)) + '#' + i
        return s
    
    
    def decode(self, s: str) -> List[str]:
        n = 0
        words = []
        while n < len(s):
            j = n
            while s[j] != '#':
                j += 1
            lit = int(s[n:j])
            n = j + 1
            j = n + lit
            words.append(s[n:j])
            n = j
        return words