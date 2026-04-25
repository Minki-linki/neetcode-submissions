class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_doubles = {}

        for num in nums:
            dict_doubles[num] = 1 + dict_doubles.get(num, 0)
        
        cnt_spok = []
        for cnt, ind in sorted(dict_doubles.items(), key= lambda x: x[1], reverse= True):
            cnt_spok.append(cnt)
            if len(cnt_spok) == k:
                return cnt_spok
                