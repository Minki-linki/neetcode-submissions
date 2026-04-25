class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_doubles = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            dict_doubles[num] = 1 + dict_doubles.get(num, 0)
        for num, cnt in dict_doubles.items():
            freq[cnt].append(num)

        results = []
        for res in range(len(freq) -1, 0, -1):
            for result in freq[res]:
                results.append(result)
                if len(results) == k:
                    return results
       
                