class Solution:
    #O(m+n)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        nums1.sort()
        print(nums1)
        nums2.sort()
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):         
            if(nums1[i]>nums2[j]):
               
                j+=1
            elif(i>0 and nums1[i]==nums1[i-1]):
                i+=1
            elif (nums1[i]<nums2[j]  ):
                i+=1
               
            elif (j>0 and nums2[j]==nums2[j-1]):
                j+=1
            elif nums1[i]==nums2[j] :
                result.append(nums1[i])
                i+=1
                j+=1
        return result
                    
        
