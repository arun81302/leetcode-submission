class Solution(object):
    def rotate(self, arr, k):
        n=len(arr)
        k=k%n
        def check(arr,i,j):
            j=j-1
            while i<j:
                
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        check(arr,0,n-k)
        check(arr,n-k,n)
        check(arr,0,n)
        return arr
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        