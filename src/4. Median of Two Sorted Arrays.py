class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        i=0
        j=0
        temp=[0]*(m+n)
        count=0
        while i<m and j<n:
            if(nums1[i]<nums2[j]):
                temp[count]=nums1[i]
                count+=1
                i+=1
            else:
                temp[count]=nums2[j]
                count+=1
                j+=1
        while i<m:
            temp[count]=nums1[i]
            count+=1
            i+=1
        while j<n:
            temp[count]=nums2[j]
            count+=1
            j+=1
        if (m+n)%2!=0:
            return float(temp[int((m+n)/2)])
        else:
            return (temp[int((m+n)/2)]+temp[int((m+n)/2)-1])/2
        
            
                
                
