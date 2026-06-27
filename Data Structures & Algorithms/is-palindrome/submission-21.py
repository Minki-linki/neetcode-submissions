class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ''.join(c for c in s.lower() if c.isalnum())
        return b[::-1] == b