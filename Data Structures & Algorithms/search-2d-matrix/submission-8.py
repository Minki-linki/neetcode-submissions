class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        group_sort = []
        for i in matrix:
            group_sort.extend(i)
        
        l, r = 0,len(group_sort)-1
        
        while l <= r:
            mid = (l+r)//2

            if group_sort[mid] > target:
                r = mid - 1
            elif group_sort[mid] < target:
                l = mid + 1
            else:
                return True
        return False


        