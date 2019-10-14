class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic={5:0,10:0}
        for i in range(len(bills)):
            if bills[i]==5:
                dic[5]+=1
            elif bills[i]==10:
                if dic[5]>0:
                    dic[10]+=1
                    dic[5]-=1
                else:
                    return False
            else:
                if dic[10]>0 and dic[5]>0:
                    dic[10]-=1
                    dic[5]-=1
                elif dic[5]>=3:
                    dic[5]-=3
                else:
                    return False       
        return True
   # Judge if this could be changed . The method is more universal. But slow.
   def lemonadeChange(self, bills: List[int]) -> bool:
        dic={5:0,10:0,20:0}
        for i in range(len(bills)):
            if self.change(dic,bills[i]-5):
                print(bills[i],"can change it")
                dic[bills[i]]+=1
            else:
                return False
        return True
            
    def change(self,dic,money):
        while money>=10 and dic[10]>0:
            money-=10
            dic[10]-=1
        while money>=5 and dic[5]>0:
            money-=5
            dic[5]-=1
        return money==0
