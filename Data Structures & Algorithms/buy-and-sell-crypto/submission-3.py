class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        if (len(prices) == 1):
            return 0
        l, r = prices[0], prices[1]
        max_profit= r - l

        for i in range (len(prices)):
        
            if (prices[i] < l):
                l = prices[i]
               

            else:
                max_profit = max(max_profit, prices[i] - l)
                
        return max_profit

           
        