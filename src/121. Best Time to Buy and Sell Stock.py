class Solution:
    # Kadane's Algorithm.
    # If the maxCur<0, means that the curVal is less than the lastMinValue
    def maxProfit(self, prices: List[int]) -> int:
        maxCur,maxSoFar=0,0
        for i in range(1,len(prices)):
            maxCur=max(0,maxCur+prices[i]-prices[i-1])
            maxSoFar=max(maxCur,maxSoFar)
        return maxSoFar
    def maxProfit1(self, prices: List[int]) -> int:
        min_price,profit=float('inf'),0
        for price in prices:
            min_price=min(min_price,price)
            profit=max(profit,price-min_price)
        return profit
