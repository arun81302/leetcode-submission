class Solution(object):
    def sortedSquares(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)):
            if arr[i]<0:
                arr[i]=arr[i]*(-1)
        arr.sort()
        for i in range(len(arr)):
            arr[i]=arr[i]*arr[i]
        return arr
        