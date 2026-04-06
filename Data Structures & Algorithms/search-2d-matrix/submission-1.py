class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowSize = len(matrix[0]) - 1
        
        low, high = 0, len(matrix) - 1
        mid = low + (high - low) // 2

        targetRow = -1
        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] <= target <= matrix[mid][rowSize]:
                targetRow = mid
                break

            elif matrix[mid][0] <= target and matrix[mid][rowSize] <= target:
                low = mid + 1
            
            else:
                high = mid - 1

        if targetRow == -1:
            return False

        low, high = 0, rowSize
        mid = low + (high - low) // 2

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[targetRow][mid] == target:
                return True

            elif matrix[targetRow][mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False




