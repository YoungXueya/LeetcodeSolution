class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        for item in A:
            if item %2==0:
                even.append(item)
        
            else:
                odd.append(item)
        return even+odd
