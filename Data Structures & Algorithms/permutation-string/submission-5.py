class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        for s in s1:
            count1[s] = 1 + count1[s]


        for i in range(len(s2)):

            if (s2[i] not in count1):
                continue
            jump = i + len(s1) 

            while (i < jump and i < len(s2)):
                count2[s2[i]] = 1 + count2[s2[i]]
                i+= 1

            if count1 == count2:
                return True
            else:
                count2.clear()
    
        return False

   

        
       


        