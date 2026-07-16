class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        print(sorted(nums))

       
        

        for i in range(len(nums)-1):

            l = i + 1
            r = len(nums) - 1


            if i > 0 and nums[i] == nums[i - 1]:
                continue

        
            while (l < r):
                curr_sum = nums[i] + nums[l] + nums[r]
                
                if (curr_sum > 0):
                    r-= 1 
                elif (curr_sum < 0):
                    l+= 1
                else:
                    temp = [nums[i], nums[l], nums[r]]
                    res.append(temp)
                    l+= 1
                    while (nums[l] == nums[l-1] and l < r ):
                        l+= 1

        return res

        