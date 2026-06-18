class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            word = [0] * 26
            for j in i:
                word[ord(j) - ord('a')] += 1
            key = tuple(word)
            if key not in res:
                res[key] = []
            res[key].append(i)
        
        return list(res.values())