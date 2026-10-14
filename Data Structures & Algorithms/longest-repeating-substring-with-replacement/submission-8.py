class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        max_length = 0
        d = {}
        left, right = 0, 0

        while right != len(s):
            d[s[right]] = d.get(s[right], 0) + 1
            max_freq = max(d.values())
            length = right - left + 1
            res = length - max_freq
            if res <= k:
                max_length = max(max_length, length)
            else:
                d[s[left]] -= 1
                left += 1
            right += 1
        return max_length
