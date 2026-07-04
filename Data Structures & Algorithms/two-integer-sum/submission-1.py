class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        indices_list = []

        for i in range(len(nums)):

            diff = target - nums[i]
            print(diff)

            if diff in hashmap:
                indices_list.append(hashmap.get(diff))
                indices_list.append(i)

                print(hashmap.get(i))
                
                return indices_list

            else:
                hashmap[nums[i]] = i

            


        