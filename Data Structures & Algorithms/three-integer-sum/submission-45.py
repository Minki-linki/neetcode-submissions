class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        group_nums = list()

        for ind, left in enumerate(nums):
            if nums[ind - 1] == nums[ind] and ind > 0:
                continue
            if nums[ind] > 0:
                break
            central = ind + 1
            right = len(nums) - 1
            while central < right:
                if nums[ind] + nums[central] + nums[right] > 0:
                    right -= 1
                elif nums[ind] + nums[central] + nums[right] < 0:
                    central += 1
                else:
                    group_nums.append([nums[ind], nums[central], nums[right]])
                    central +=1
                    right -= 1
                    while central < right and nums[central] == nums[central - 1]:
                        central += 1
                    
        return group_nums
                