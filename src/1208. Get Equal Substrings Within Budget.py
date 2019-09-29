class Solution:
    def equalSubstring(self,s, t, maxCost):
        diff=[abs(ord(i)-ord(j)) for i,j in zip(s,t)]
        print(diff)
        start=0
        maxCount=0
        sumDiff=0
        for i in range(len(s)):
            sumDiff+=diff[i]
            while sumDiff>maxCost:
                sumDiff-=diff[start]
                start+=1
            maxCount=max(maxCount,i - start +1)
        return maxCount
