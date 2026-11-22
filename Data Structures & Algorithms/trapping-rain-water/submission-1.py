class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = right = 0

        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        
        
        j = 0

        for i in range(n):

            j-= 1

            max_left[i] = left
            max_right[j] = right

            left = max(left, height[i])
            right = max(right, height[j])

        sum = 0
        for i in range(n):
            potential_sum = min(max_left[i], max_right[i])         
            sum+= max(0, potential_sum - height[i])
            
        return sum
        
        





        