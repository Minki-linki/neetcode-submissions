class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_words = defaultdict(list)
        for word in strs:
            container = [0] * 26
            for c in word:
                container[ord(c) - ord('a')] += 1
            key = tuple(container)
            dict_words[key].append(word)
        return list(dict_words.values())