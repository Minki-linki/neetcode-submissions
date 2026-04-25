class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            container = [0] * 60
            for i in range(len(s)):
                container[ord(s[i]) - ord('a')] += 1
                container[ord(t[i]) - ord('a')] -= 1

            for i in container:
                if i != 0:
                    return False
            return True