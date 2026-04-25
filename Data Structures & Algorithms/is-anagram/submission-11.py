class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            l_t = 0
            dict_cnt = {}
            for i in range(len(s)):
                dict_cnt[s[i]] = dict_cnt.get(s[i],0) + 1
                dict_cnt[t[i]] = dict_cnt.get(t[i],0) - 1
            
            return all(x == 0 for x in dict_cnt.values())
        else:
            return False