class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

       
        product = 1

        index = set()

        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                index.add(i)
                continue
            product = product * nums[i]

        
        for i in range(len(nums)):
            if len(index) > 1:
                res[i] = 0
                continue

            if len(index) == 1 and i in index:
                res[i] = product
                continue
            elif (len(index) == 1):
                res[i] = 0
                continue
            
            else:
                res[i] = product // nums[i]

        return res
            


        