class Solution(object):
    def shuffle(self, arr, n):
        res=[0]*(2*n)
        i=0
        a=0
        while i<n:
            res[a]=arr[i]
            i+=1
            a+=2
        i=n
        a=1
        while i<len(arr):
            res[a]=arr[i]
            i+=1
            a+=2
        return res


        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        