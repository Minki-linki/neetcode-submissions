class Solution:
    def isPalindrome(self, s: str) -> bool:
        sortcnt = ''
        for i in s.lower():
            if i.isalnum():
                sortcnt += i
        return sortcnt == sortcnt[::-1]