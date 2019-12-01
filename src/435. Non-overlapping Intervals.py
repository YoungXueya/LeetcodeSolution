# This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[1])
        curRight=-float('inf')
        count=0
        for x in intervals:
            if x[0]>=curRight:
                curRight=x[1]
            else:
                count+=1
            
            
        return count
        
