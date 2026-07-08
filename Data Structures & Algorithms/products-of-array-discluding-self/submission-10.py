class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 'result' stores the running prefix products and 
        # is eventually repurposed to hold the final answer
        result = [0] * len(nums)
        postfix_product = 1
        
        # Calculate prefix products
        for i in range(len(nums)):
            if i == 0:
                result[i] = nums[i]
            else:
                result[i] = nums[i] * result[i - 1]
                
        print(result)
        
        # Calculate postfix products and combine with prefix to get final result
        for i in range(len(nums) - 1, -1, -1):
            if i == (len(nums) - 1):
                result[i] = result[i - 1]
                postfix_product = nums[i]
                continue
                
            if i == 0:
                result[i] = postfix_product
                break
                
            result[i] = result[i - 1] * postfix_product
            postfix_product = postfix_product * nums[i]
            
        print(result)
        
        return result