class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        visited={}
        def maxscore(i,j):
            if i>=j:
                return 0
            if j==i+1 and j<len(piles):
                return piles[i]
            if (i,j) in visited:
                return visited[i,j]
            # This is a process that Alex want to get the maximum after this choice
            # While Lee want Alex get minmum after this choice.
            result=	 max(piles[i]+min(maxscore(i+2,j), maxscore(i+1,j-1)) , piles[j-1] + min(maxscore(i+1,j-1), maxscore(i,j-2)))

            visited[i,j]=result
            return result
        scoreA=maxscore(0,len(piles))
        print(scoreA)
        scoreL=sum(piles)-scoreA
        return scoreA>scoreL
        
