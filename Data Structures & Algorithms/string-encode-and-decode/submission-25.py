class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for st in strs:
            code += str(len(st)) + ' ' + st
        return code


    def decode(self, s: str) -> List[str]:
        left = 0
        right = 0
        box = []
        while right != len(s):
            while s[left] != ' ':
                left += 1
            length = int(s[right:left])
            left += 1 
            right = left + length   
            phrases = s[left : right]
            box.append(phrases)
            left = right
        return box

