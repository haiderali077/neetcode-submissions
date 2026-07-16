class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] 
        res = [0] * len(temperatures)
        max_temp = 0
        index = 0

    

        for i in range(len(temperatures)):
            print(stack)
            

          


            if not stack:
                stack.append((temperatures[i], i))
                continue

            else:
                while stack[-1][0] < temperatures[i]:
                
                    print(stack[-1][0], temperatures[i], i)
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                    if not stack:
                        break
            stack.append((temperatures[i], i))

        return res

        # REFRESHER: Monotonic Stack (Next Greater Element)
# We push (temp, index) onto the stack to keep track of previous days awaiting a warmer temperature. 
# As we iterate, if the current temperature is warmer than the top of the stack, it means we've found the 
# next greater day; we pop the stack and calculate the wait time (current_i - old_i) for those popped days.



            



        