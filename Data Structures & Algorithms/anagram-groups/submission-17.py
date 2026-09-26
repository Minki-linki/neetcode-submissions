class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        box = {}
        for w in strs:
            words = [0] * 30
            for word in range(len(w)):
                words[ord(w[word]) - ord('a')] += 1
            words = tuple(words)
            if words not in box:
                box[words] = [] 
            box[words].append(w)
        
        return list(box.values())