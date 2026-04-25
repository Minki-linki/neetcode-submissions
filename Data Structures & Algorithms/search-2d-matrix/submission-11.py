class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row =[]

        for i in matrix:
            left = 0
            right = len(i) - 1
            while left <= right:
                diff = (left + right)//2
                if i[diff] < target:
                    left = diff + 1
                elif i[diff] > target:
                    right = diff - 1
                else: 
                    return True
        return False

        