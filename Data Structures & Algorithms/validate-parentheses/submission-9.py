class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) >= 2:

            PROVERKA = {
                ')':'(',
                '}':'{',
                ']':'['
            }
            provrk_list = []
            for i in range(len(s)):
                if s[i] in PROVERKA.values():
                    provrk_list.append(s[i])
                if s[i] in PROVERKA.keys():
                    if not provrk_list:
                        return False
                    if PROVERKA[s[i]] != provrk_list.pop():
                        return False
            
            return len(provrk_list) == 0
        else:
            return False
