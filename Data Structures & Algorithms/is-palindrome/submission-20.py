class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if (len(s) == 1 or len(s) == 0):
            return True

        s = s.replace(" ", "")

        


     
    
        l, r = 0, len(s)-1

       
    
        for i in range(len(s)-1):

            print(i)

          

            if (s[l].isalnum() == False):
                l+= 1
                continue 

            if (s[r].isalnum() == False):
                r-= 1
                continue


            if (s[l].lower() == s[r].lower()):
                l+= 1
                r-= 1
            else:
                return False

        return True


        