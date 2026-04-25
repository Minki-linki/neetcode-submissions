class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for i in nums:
            if i not in group:
                group[i] = 0
            group[i] += 1
        
        return sorted(group, key= group.get, reverse= True)[:k]