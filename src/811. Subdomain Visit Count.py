class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic={}
        for item in cpdomains:
            num,domain=item.split(" ")
            num=int(num)
            subdomain=domain.split(".")
            for i in range(len(subdomain)):
                dom=".".join(subdomain[i:])
                if dom in dic:
                    dic[dom]+=num
                else:
                    dic[dom]=num
        
        result=[]
        for item in dic:
            res=str(dic[item])+" "+item
            result.append(res)
        return result
        
