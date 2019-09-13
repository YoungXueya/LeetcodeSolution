class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        right=sorted(heights)
        count=0
        for i in range(len(heights)):
            if right[i]!=heights[i]:
                count+=1
        return count
        
