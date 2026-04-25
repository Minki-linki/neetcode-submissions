class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anogram = {}
        for i in strs:
            if ''.join(sorted(i)) not in anogram:
                anogram[''.join(sorted(i))] = [i]
            else:
                anogram[''.join(sorted(i))] += [i]
        return list(anogram.values())