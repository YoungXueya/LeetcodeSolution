class Solution:
    def rotatedDigits(self, N: int) -> int:
        dic={"0":"0","1":"1","2":"5","5":"2","6":"9","8":"8","9":"6"}
        count=0
        for i in range(1,N+1):
            isValid=True
            old=str(i)
            print(old)
            new=""
            for ch in old:
                if ch not in dic.keys():
                    isValid=False
                    break
                else:
                    new+=dic[ch]
            if isValid and new !=old:
                count+=1
        return count
