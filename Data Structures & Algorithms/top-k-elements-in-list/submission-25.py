class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        bucket = [[] for i in range(len(nums) + 1)]
        for i in nums:
            res[i] = res.get(i, 0) + 1
        for num, frq in res.items():
            bucket[frq].append(num)
        
        t = []
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                t.append(num)
                if len(t) == k:
                    return t