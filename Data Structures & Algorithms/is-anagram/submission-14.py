class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = [0] * 26
        for i in range(len(s)):
            n[ord(s[i]) - ord('a')] += 1
            n[ord(t[i]) - ord('a')] -= 1
        for i in n:
            if i != 0:
                return False
        return True