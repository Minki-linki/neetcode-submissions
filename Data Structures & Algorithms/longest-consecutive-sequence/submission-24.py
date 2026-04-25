class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            best = 0
            for i in set(nums):
                if i - 1  in nums:
                    continue
                else:
                    cur = i
                    lek = 1
                    while cur + 1 in nums:
                        cur += 1
                        lek += 1
                    best = max(best, lek)
            return best