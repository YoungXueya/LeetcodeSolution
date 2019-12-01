class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies=[1 for i in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i]=max(candies[i],candies[i-1]+1)
            # print(candies)
        # print(len(ratings))
        for i in range(len(ratings)-2,-1,-1):
            # print(i)
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i],candies[i+1]+1)
            # print(candies)
        return sum(candies)
        
