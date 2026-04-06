class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prof = 0

        buy = prices[0]            
        for i in range(len(prices)):
            todayProfit = prices[i] - buy

            if prices[i] < buy:
                buy = prices[i]

            prof = max(prof, todayProfit)
            
        return prof