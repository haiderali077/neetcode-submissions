class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            if (i == 0):
                prefix[i] = nums[i]
        
            else:
                prefix[i] = nums[i] * prefix[i - 1]
              
                
  
        

        for i in range(len(nums) -1, -1, -1):
            if (i == (len(nums) - 1)):
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i + 1]

        
        for i in range(len(nums)):
            if (i == 0):
                res[i] = postfix[i+1]
                continue
            if (i == (len(nums) - 1)):
                res[i] = prefix[i-1]
                continue
            
            res[i] = prefix[i -1] * postfix[i+1]


            



   
               
          

      
                
        


        return res


    

        
                


        

                

        