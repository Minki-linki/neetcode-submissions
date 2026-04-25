class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, k = 0, len(numbers) - 1

        while l != k:
            if numbers[l] + numbers[k] > target:
                k -= 1
            elif numbers[l] + numbers[k] < target:
                l += 1
            else:
                return [l+1, k+1]
