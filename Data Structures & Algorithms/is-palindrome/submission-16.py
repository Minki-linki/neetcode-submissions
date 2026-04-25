class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, k = 0, len(s) - 1

        while l < k:
            while l< k and not s[l].isalnum():
                l += 1
            while k> l and not s[k].isalnum():
                k -= 1
            if s[l].lower() != s[k].lower():
                return False
            l, k =l + 1, k - 1
        return True