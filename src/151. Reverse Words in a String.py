class Solution(object):
    # Kowns how to use split() " ".join(),and reverse index
    def reverseWords(self,s):
        return " ".join(s.split()[::-1])
        
    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        splited=s.split(" ")
        start=True
        result=""
        for i in range(-1,-len(splited)-1,-1):
            
            if(splited[i]):
               
                if (start):
                    result=splited[i]
                    start=False
                else:        
                    result+=" "+splited[i]
        return result
