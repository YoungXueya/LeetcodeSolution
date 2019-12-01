# Whenever the sum is negative, reset it and let the car start from next point.
# In the mean time, add up all of the left gas to total. If it's negative finally, return -1 since it's impossible to finish.
# If it's non-negative, return the last point saved in res;
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    
        tank=0
        rest=0
        res=0
        for i in range(len(gas)):
            tank+=gas[i]
            tank-=cost[i]
            if tank<0:
                rest+=tank
                tank=0
                res=i+1
        if tank+rest>=0:
            return res
        else:
            return -1
