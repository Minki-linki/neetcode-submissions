class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anogram = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in anogram:
                anogram[key] = [i]
            else:
                anogram[key] += [i]
        return list(anogram.values())