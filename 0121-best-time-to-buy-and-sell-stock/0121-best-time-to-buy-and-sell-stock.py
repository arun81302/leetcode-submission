class Solution(object):
    def maxProfit(self, arr):
        minvalue=arr[0]
        maxvalue=0
        res=0
        for i in arr:
            minvalue=min(minvalue,i)
            res=i-minvalue
            maxvalue=max(res,maxvalue)
        return maxvalue

        """
        :type prices: List[int]
        :rtype: int
        """
        