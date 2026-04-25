class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt_nums = {}
        for i in nums:
            cnt_nums[i] = cnt_nums.get(i, 0) + 1
            if cnt_nums[i] > 1:
                return True
           
        return False