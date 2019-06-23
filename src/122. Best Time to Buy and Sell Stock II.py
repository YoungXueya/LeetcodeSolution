class Solution:
    # Plus until prrices falls,that is (prices[i]-prices[i-1])<0
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(1,len(prices)):
            res+=max(0,prices[i]-prices[i-1])
        return res
        
