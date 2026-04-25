class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, t = 0, len(s)-1
        s = s.lower()

        while l < t:
            while l < t and not s[l].isalnum():
                l += 1
            while l < t and not s[t].isalnum():
                t -= 1
            if s[l].lower() != s[t].lower():
                return False
            else:
                l += 1
                t -= 1
        return True