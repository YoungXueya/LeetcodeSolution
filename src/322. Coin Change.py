class Solution(object):
    # Dynamic programming
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        count=[amount+1]*(amount+1)
        count[0]=0
        for i in range(amount+1):
            for c in coins:
                if i>=c:
                    # print(i-c,count[i-c])
                    count[i]=min(count[i],count[i-c]+1)
                    # print(count[i])
        
        if count[-1]>amount:
            return -1
        else:
            return count[-1]
