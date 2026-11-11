class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        hashmap = {}

        for n in nums:
            hashmap[n]  = hashmap.get(n, 0) + 1;
            if hashmap[n] > 1:
                return n

        