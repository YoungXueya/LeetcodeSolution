class Solution:
    # Select the top N who could fly to A saving more money than go to B
    # Then the last N is the one that using less money to B than A.
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        count=0
        costs=sorted(costs,key=lambda diff:diff[0]-diff[1])
        # print(result)
        half=int(len(costs)/2)
        for i in range(half):
            count+=costs[i][0]+costs[i+half][1]
        
        return count
