class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix)*len( matrix[0])) - 1
        while left <= right:
            diff = (left + right)//2
            row = diff // len(matrix[0])
            cols = diff % len(matrix[0])
            if matrix[row][cols] < target:
                left = diff + 1
            elif matrix[row][cols] > target:
                right = diff - 1
            else: 
                return True
        return False

        