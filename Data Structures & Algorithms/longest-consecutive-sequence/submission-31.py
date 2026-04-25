class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) != 0: 
            num_set = set(nums)
            max_cnt = 0
            for num in num_set:
                if (num - 1) not in num_set:
                    cnt = 1
                    cnt_num = num
                    while (cnt_num + 1) in num_set:
                        cnt += 1
                        cnt_num += 1
                    max_cnt = max(cnt,max_cnt)
            return max_cnt
        return 0