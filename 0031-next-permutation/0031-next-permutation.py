class Solution(object):
    def nextPermutation(self, arr):
        idx=-1
        for i in range(len(arr)-2,-1,-1):
            if arr[i]<arr[i+1]:
                idx=i
                break
        if idx==-1:
            arr.sort()
            return arr
        maxidx=0
        for i in range(len(arr)-1,idx,-1):
            if arr[i]>arr[idx]:
                maxidx=i
                break
        i=idx+1
        j=len(arr)-1
        arr[idx],arr[maxidx]=arr[maxidx],arr[idx]
        while i<=j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        return arr

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        