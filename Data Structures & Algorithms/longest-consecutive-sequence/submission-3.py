class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if (len(nums) == 0):
            return 0

        
        hashmap = {}

        for i in range(len(nums)):
            if (nums[i] in hashmap.values()):
                continue
            hashmap[i] = nums[i]
        
        print(hashmap)

        
        max_count = 0
        for key, value in hashmap.items():
            curr_count = 0

            if ((value - 1) not in hashmap.values()):
                curr_count += 1

                while ((value + 1) in hashmap.values()):
                    curr_count += 1
                    value+= 1

                max_count = max(curr_count, max_count)


        print(max_count)

    
        return max_count
        