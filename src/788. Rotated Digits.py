class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        Max=-1
        last=-1
        flag=True
        for i in range(len(seats)):
            if seats[i]==0:
                if i==len(seats)-1:
                    print("Here")
                    Max=max(Max,len(seats)-1-last)
                continue
            else:
                print("last",last)
                print("Max",Max)
                if last==-1:
                    Max=max(i,Max)
                
                else:
                    Max=max(Max,(i-last)/2)
                last=i
        return int(Max)
