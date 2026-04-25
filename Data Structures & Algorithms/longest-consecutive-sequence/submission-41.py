class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            nums = set(nums)
            max_cnt = 0
            for i in nums:
                if (i-1) not in nums:
                    cnt = 1
                    while (i + cnt) in nums:
                        cnt += 1
                    max_cnt = max(max_cnt,cnt)
            return max_cnt
