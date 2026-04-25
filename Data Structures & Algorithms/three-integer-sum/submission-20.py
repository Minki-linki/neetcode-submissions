class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        stack_group = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0:
                break
            
            if i > 0 and val == nums[i-1]:
                continue

            l, t = i + 1, len(nums) - 1

            while l < t:
                if val + nums[l] + nums[t] > 0:
                    t -= 1
                elif val + nums[l] + nums[t] < 0:
                    l += 1
                else:
                    stack_group.append([val, nums[l], nums[t]])
                    l += 1
                    t -= 1
                    while (nums[l] == nums[l-1] and l < t) and (nums[t] == nums[t+1] and l < t): l += 1
        return stack_group 
