class Solution(object):
    def merge(self, arr, m, brr, n):
        if m==0 and n!=0:
            i=0
            j=0
            while j<n:
                arr[i]=brr[j]
                j+=1
                i+=1
        if n==0:
            return arr
        i=m-1
        j=n-1
        k=(m+n)-1
        while i>=0 and j>=0:
            if arr[i]>brr[j]:
                arr[k]=arr[i]
                i-=1
            else:
                arr[k]=brr[j]
                j-=1
            k-=1
        while j>=0:
            arr[k]=brr[j]
            j-=1
            k-=1

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        