class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix = [0] * len(nums)
        postfix = 1
        

        for i in range(len(nums)):
            if (i == 0):
                prefix[i] = nums[i]
        
            else:
                prefix[i] = nums[i] * prefix[i - 1]

        print(prefix)


        for i in range(len(nums) -1, -1, -1):
            if (i == (len(nums) - 1)):     
                prefix[i] = prefix[i-1]
                postfix = nums[i]
                
                continue

            if (i == 0):
                prefix[i] = postfix
                continue

            
            
           

           
            prefix[i] = prefix[i-1] * postfix
            postfix = postfix * nums[i]
        
        print(prefix)
      

            
        return prefix


    

        
                


        

                

        