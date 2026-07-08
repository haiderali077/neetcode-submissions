class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if (len(nums) == 0):
            return 0

        
        hashmap = {}

        for n in nums:
            if (n in hashmap):
                continue
            hashmap[n] = n

        max_count = 0
        for key in hashmap:
            curr_count = 0

            if ((key-1) not in hashmap):
                curr_count += 1

                while ((key + 1) in hashmap):
                    curr_count += 1
                    key+= 1

                max_count = max(curr_count, max_count)


        print(max_count)

    
        return max_count
        