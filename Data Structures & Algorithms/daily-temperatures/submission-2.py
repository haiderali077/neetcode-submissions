class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] 
        res = [0] * len(temperatures)
       

    

        for i in range(len(temperatures)):
            print(stack)
            if not stack:
                stack.append((temperatures[i], i))
                continue

            else:
                while stack[-1][0] < temperatures[i]:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                    if not stack:
                        break
            stack.append((temperatures[i], i))

        return res


            



        