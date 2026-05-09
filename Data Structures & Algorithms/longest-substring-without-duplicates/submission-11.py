class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_uniqe = dict()
        left, max_count = 0, 0

        for i in range(len(s)):
            if s[i] in dict_uniqe and left <= dict_uniqe[s[i]]:
                left = dict_uniqe[s[i]] + 1
                dict_uniqe[s[i]] = i
            else:
                dict_uniqe[s[i]] = i
            max_count = max(max_count, i - left + 1)
        return max_count