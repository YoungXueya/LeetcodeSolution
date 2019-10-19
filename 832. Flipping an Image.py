class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[x[::-1] for x in A]
        # print(res)
        
        res=[[x^1 for x in y] for y in res]
        return res
        
