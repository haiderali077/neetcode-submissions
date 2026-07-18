from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # Row boundaries for the outer binary search
        top_row, bottom_row = 0, len(matrix) - 1
        
        # Track the last column index to check row boundaries
        last_col_idx = len(matrix[0]) - 1

        while top_row <= bottom_row:
            mid_row = (top_row + bottom_row) // 2
          
            # If target is larger than the largest element in this row, look down
            if target > matrix[mid_row][last_col_idx]:
                top_row = mid_row + 1
                
            # If target is smaller than the smallest element in this row, look up
            elif target < matrix[mid_row][0]:
                bottom_row = mid_row - 1
                
            # Otherwise, the target must be within this specific row
            else:
                # Column boundaries for the inner binary search
                left_col, right_col = 0, last_col_idx
                
                while left_col <= right_col:
                    mid_col = (left_col + right_col) // 2

                    if matrix[mid_row][mid_col] < target:
                        left_col = mid_col + 1 
                    elif matrix[mid_row][mid_col] > target:
                        right_col = mid_col - 1 
                    else:
                        return True
                
                # If we fully searched the correct row and didn't find it, 
                # the target does not exist in the matrix.
                return False
            
        return False
