class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_cnt = defaultdict(int)
        cnt = [[] for _ in range(len(nums)+1)]
        for i in nums:
            dict_cnt[i] += 1
        for num, count in dict_cnt.items():
            cnt[count].append(num)
        res = []
        for i in range(len(cnt)-1, 0 ,-1):
            for n in cnt[i]:
                res.append(n)
                if len(res) == k:
                    return res