class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #convert to a list from a matrix
        #then do binary search?
        # flattened = [num for row in matrix for num in row]
        # left = 0
        # right = len(flattened)-1

        # while left<=right:
        #     mid = (left+right)//2
        #     if flattened[mid]==target:
        #         return True
        #     elif flattened[mid]>target:
        #         right = mid - 1
        #     else:
        #         left = mid+1

        # return False
        if not matrix or not matrix[0]:
            return False
        m,n = len(matrix),len(matrix[0])
        left, right = 0,m*n-1

        while left<=right:
            mid = (left+right)//2
            row,col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            elif val<target:
                left = mid +1
            else:
                right = mid -1
        return False
        