class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list, t_list = sorted(list(s)), sorted(list(t))
        if s_list == t_list:
            return True
        else:
            return False