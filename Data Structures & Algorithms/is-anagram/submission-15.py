class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        boxes = [0] * 30 

        for num in range(len(s)):
            boxes[ord(s[num]) - ord('a')] += 1
            boxes[ord(t[num]) - ord('a')] -= 1
        
        for o in boxes:
            if o != 0:
                return False
        return True