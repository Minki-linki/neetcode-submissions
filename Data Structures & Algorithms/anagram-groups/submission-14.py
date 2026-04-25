class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_key = {}

        for i in strs:
            s = [0] * 60
            for j in i:
                s[ord(j)-ord('a')] += 1
            key = tuple(s)

            if key in dict_key:
                dict_key[key].append(i)
            else:
                dict_key[key] = [i]
        return list(dict_key.values())