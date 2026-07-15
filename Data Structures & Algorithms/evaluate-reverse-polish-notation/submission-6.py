class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        from collections import deque
        
        if len(tokens) == 1:
            return int(tokens[0])

        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv} 

        l, r = 0, 1


        stack = []
        result = 0

        for t in tokens:
            if (t != '+') and (t != '-') and (t != '*') and (t != '/'):
                stack.append(t)
            else:
                t = chr(ord(t))
                result = ops[t](int(stack[-2]), int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(result)
        
            

        return int(result)



                


            