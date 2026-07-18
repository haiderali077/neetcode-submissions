class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = []
        stack = []

        

        for i in range(len(position)):
            pair.append((position[i], speed[i]))

        pair.sort()


        for i in range(len(pair) -1, -1, -1):
            position = (target - pair[i][0]) / pair[i][1]
        
            if not stack:
                stack.append(position)
            else:
                stack.append(position)
                
                if stack[-1] <= stack[-2]:
                    stack.pop()
                

        return len(stack)

        

        
        