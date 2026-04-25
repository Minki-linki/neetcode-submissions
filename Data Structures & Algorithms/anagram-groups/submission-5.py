class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anogram = {}
        for i in strs:
            if ''.join(sorted(list(i))) not in anogram:
                anogram[''.join(sorted(list(i)))] = [i]
            elif ''.join(sorted(list(i))) in anogram:
                anogram[''.join(sorted(list(i)))] += [i]
        return list(anogram.values())