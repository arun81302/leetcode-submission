class Solution(object):
    def check(self, arr):
        n=len(arr)
        ind=0
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                ind=i
                break
        k=len(arr)-ind
        def rotate(arr,i,j):
            j=j-1
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        rotate(arr,0,n-k)
        rotate(arr,n-k,n)
        rotate(arr,0,n)
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                return False
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        