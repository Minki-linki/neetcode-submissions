class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        z, x =0, len(numbers)-1
        while z < x:
            if numbers[z] + numbers[x] > target:
                x -= 1
            elif numbers[z] + numbers[x] < target:
                z += 1
            else:
                return [z+1, x+1]