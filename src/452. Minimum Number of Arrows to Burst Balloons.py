class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        after=sorted(points,key=lambda x:(x[1],x[1]-x[0]))
        
        cur_right=-float('inf')
        count=0

        for point in after:
            if point[0]>cur_right:
                print(cur_right)
                cur_right=point[1]
                count+=1
        return count
        
