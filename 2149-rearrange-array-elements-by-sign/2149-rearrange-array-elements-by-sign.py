class Solution(object):
    def rearrangeArray(self, arr):
        res=[0]*len(arr)
        pos=0
        neg=1
        for i in range(len(arr)):
            if arr[i]>0:
                res[pos]=arr[i]
                pos+=2
            else:
                res[neg]=arr[i]
                neg+=2
        return res

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        