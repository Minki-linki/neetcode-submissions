class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sit = set()
        max_leght = 0
        left, right = 0, 0
        
        while right != len(s):
            if s[right] not in sit:
                sit.add(s[right])
            else:
                while s[left] != s[right]:
                    sit.remove(s[left])
                    left += 1
                left += 1
            max_leght = max(max_leght, right - left + 1)
            right += 1
        return max_leght
