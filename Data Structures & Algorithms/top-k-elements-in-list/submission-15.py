class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for i in nums:
            group[i] = group.get(i, 0)+1
        
        return sorted(group, key= group.get, reverse= True)[:k]