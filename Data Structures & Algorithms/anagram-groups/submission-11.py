class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anogram = {}
        for i in strs:
            key = ''.join(sorted(i))
            anogram.setdefault(key,[]).append(i)
        return list(anogram.values())