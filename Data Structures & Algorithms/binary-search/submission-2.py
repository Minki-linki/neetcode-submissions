class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 

        while left <= right:
            diff = (left + right)//2
            if nums[diff] < target:
                left = diff + 1
            elif nums[diff] > target:
                right = diff - 1
            else:
                return diff
        return -1