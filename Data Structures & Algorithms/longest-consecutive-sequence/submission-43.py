class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        for i in set(nums):
            if (i-1) not in set(nums):
                lit = 1
                while (i+lit) in set(nums):
                    lit += 1
                best = max(best,lit)
        return best