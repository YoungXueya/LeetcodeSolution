class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res=[0 for i in range(n)]
        stack=[]
        prev_time=0
        for i in range(len(logs)):
            s=logs[i].split(":")
            Id,Type,Time=int(s[0]),s[1],int(s[2])
            if Type=="start":
                if stack:
                    res[stack[-1]]+=Time-prev_time
                stack.append(Id)
                prev_time=Time
            else:
                res[stack.pop()]+=Time-prev_time+1
                prev_time=Time+1
        return res
