class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  
        best = 0
        for i in num_set:
            if (i-1) not in num_set:
                lit = 1
                while (i+lit) in num_set:
                    lit += 1
                best = max(best,lit)
        return best