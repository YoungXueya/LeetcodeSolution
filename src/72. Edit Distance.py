class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        count=[[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        
        for i in range(len(word1)+1):
            count[0][i]=i
        for j in range(len(word2)+1):
            count[j][0]=j
            
        for j in range(len(word2)):
            for i in range(len(word1)):
                
                if word1[i]==word2[j]:
                    count[j+1][i+1]=count[j][i]
                else:
                    count[j+1][i+1]=min(count[j][i+1],count[j+1][i],count[j][i])+1
                # print(j+1,i+1,count[j+1][i+1])
                
        return count[len(word2)][len(word1)]
                    
        
