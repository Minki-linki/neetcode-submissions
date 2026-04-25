class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anogram = {}
        for i in strs:
            if tuple(sorted(i)) not in dict_anogram:
                dict_anogram[tuple(sorted(i))] = [i]
            elif  tuple(sorted(i)) in dict_anogram:
                dict_anogram[tuple(sorted(i))] += [i]
        return [i for i in dict_anogram.values()]
