class Solution:

    def encode(self, strs: List[str]) -> str:
        strok = ''
        for i in strs:
            strok += str(len(i)) + '#' + i
        return strok
    
    
    def decode(self, s: str) -> List[str]:
        i = 0
        spok = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            chislo = int(s[i:j])
            i = j + 1
            j = i + chislo
            spok.append(s[i:j])
            i = j
        return spok