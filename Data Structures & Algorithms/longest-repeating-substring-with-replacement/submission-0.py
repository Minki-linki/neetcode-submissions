class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_a = {}
        alf = 0
        res = 0
        L = 0
        for i in range(len(s)):
            dict_a[s[i]] = dict_a.get(s[i], 0) + 1
            alf = max(alf, dict_a[s[i]])
            
            while (i - L + 1) - alf > k :
                dict_a[s[L]] -= 1
                L += 1
            res = max(res, i - L + 1)
        return res
        
            
