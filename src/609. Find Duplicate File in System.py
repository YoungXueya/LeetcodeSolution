class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic={}
        res=[]
        for i in range(len(paths)):
            path=paths[i].split(" ")
            for i in range(1,len(path)):
                name,content=path[i].split('(')
                if content not in dic:
                    dic[content]=[path[0]+"/"+name]
                else:
                    dic[content].append(path[0]+"/"+name)
        for item in dic:
            if len(dic[item])>1:
                res.append(dic[item])
        return res
