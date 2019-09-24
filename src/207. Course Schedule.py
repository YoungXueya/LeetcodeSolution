class Solution:
    # Using visited to maintain the status of the nodes
    # If the node is visited and status is 1, means this node has no ring.
    # This works better than using Boolean, because boolean could only maintain the status visited or not in this time.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for i in range(numCourses)]
        visited=[0 for i in range(numCourses)] 
        for x,y in prerequisites:
            graph[x].append(y)
        def dfs(graph,visited,i):
            # print(i,graph[i])
            if visited[i]==-1:
                return False
            if visited[i]==1:
                return True
            
            visited[i]=-1
            for j in graph[i]:
                # print("visiting",j)
                if not dfs(graph,visited,j):
                    return False
            visited[i]=1
            return True
        for i in range(numCourses):
            if not dfs(graph,visited,i):
                return False
        return True
    # Using boolean to record the status.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for i in range(numCourses)]
        visited=[False for i in range(numCourses)] 
        for x,y in prerequisites:
            graph[x].append(y)
        def dfs(graph,visited,i):
            # print(i,graph[i])
            if visited[i]:
                return False
            else:
                visited[i]=True
            for j in graph[i]:
                # print("visiting",j)
                if not dfs(graph,visited,j):
                    return False
            visited[i]=False
            return True
        for i in range(numCourses):
            if not dfs(graph,visited,i):
                return False
        return True
            
            

        
        
                
        
            
            

        
        
                
        
