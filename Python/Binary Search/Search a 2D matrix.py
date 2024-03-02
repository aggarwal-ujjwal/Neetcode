class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m,n = len(matrix),len(matrix[0])
        right = m*n - 1

        while(left <= right) :
            mid = (left+right)//2

            if matrix[mid//n][mid%n] == target :
                return True
            elif matrix[mid//n][mid%n] < target:
                left = mid +1
            else:
                right = mid -1

        return False
