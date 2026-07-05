class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        

        if (len(prices) == 1):
            return 0

        l = prices[0]
        max_profit = 0
    

        for p in prices:
        
            if p < l:
                l = p
            else:
                max_profit = max(max_profit, p - l)    
                
        return max_profit

           
        