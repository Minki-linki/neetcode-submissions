class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_dict = {}
        if len(s) == len(t):
            for i in s:
                cnt_dict[i] = cnt_dict.get(i, 0) + 1
            for j in t:
                if j in cnt_dict and cnt_dict[j] == t.count(j):
                    continue
                else:
                    return False
            return True
        else:
            return False