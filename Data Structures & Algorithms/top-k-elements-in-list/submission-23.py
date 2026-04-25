class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic_nums = dict()
        for i in nums:
            if i not in dic_nums:
                dic_nums[i] = 1
            else:
                dic_nums[i] += 1
        return sorted(dic_nums, key= lambda x: dic_nums[x])[-k:]