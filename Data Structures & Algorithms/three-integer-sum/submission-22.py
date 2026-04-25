class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        stack_numbers =[]
        nums.sort()
        

        if min(nums)> 0:
            return []
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                l, r = i + 1, len(nums) - 1
                while l < r:
                    if nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    elif nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    else:
                        stack_numbers.append([nums[i], nums[l], nums[r]])
                        r -= 1
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
            return stack_numbers
