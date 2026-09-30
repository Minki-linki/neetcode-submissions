class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        grouped_dict = {}

        for num in nums:
            if num not in grouped_dict:
                grouped_dict[num] = 0
            grouped_dict[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for buck in grouped_dict:
            bucket[grouped_dict[buck]].append(buck)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
            
            if len(res) == k:
                return res