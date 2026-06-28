class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        right = len(nums) - 1
        nums.sort()
        group_nums = list()

        for left in range(len(nums)):
            if nums[left - 1] == nums[left] and left > 0:
                continue
            central = left + 1
            right = len(nums) - 1
            while central < right:
                if nums[left] + nums[central] + nums[right] > 0:
                    right -= 1
                elif nums[left] + nums[central] + nums[right] < 0:
                    central += 1
                else:
                    group_nums.append([nums[left], nums[central], nums[right]])
                    central +=1
                    right -= 1
                    while central < right and nums[central] == nums[central - 1]:
                        central += 1
                    while central < right and nums[right] == nums[right + 1]:
                        right -= 1
        return group_nums
                