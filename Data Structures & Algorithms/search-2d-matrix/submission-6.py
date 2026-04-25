class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        group_sort = []
        for i in matrix:
            group_sort.extend(i)
        def isCorrect( n):
            if n > target:
                return 1
            elif n < target:
                return -1 
            else:
                return 0

        l, r = 0,len(group_sort)-1
        
        while l <= r:
            mid = (l+r)//2

            if isCorrect(group_sort[mid]) > 0:
                r = mid - 1
            elif isCorrect(group_sort[mid]) < 0:
                l = mid + 1
            else:
                return True
        return False


        