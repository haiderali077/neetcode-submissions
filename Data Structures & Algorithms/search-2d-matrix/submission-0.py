class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

       
    
        l , r = 0, len(matrix) - 1 # 2

        n = len(matrix[0]) - 1  # 3


        while l <= r:
            m = (l + r) // 2 # (0 + 2) // 2 = 1
          
            

            if (target > matrix[m][n]): # [1][3]
                print("if")
                print (l, r, m)
                l = m + 1
                
                
                
            elif (target < matrix[m][n] and target < matrix[m][0]): # [1][3]
                print("elif")
                print (l, r, m)
                r = m - 1 # r = 0 
            else:
                i,  j = 0, n
                while i <= j:
                    k = (i + j) // 2

                    if matrix[m][k] < target:
                        i = k + 1 
                    elif matrix[m][k] > target:
                        j = k - 1 
                    else:
                        return True
                return False
            
            
        return False

                    

        
        
        