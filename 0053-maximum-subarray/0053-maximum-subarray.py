class Solution(object):
    def maxSubArray(self, arr):
        sumvalue=0
        maxvalue=float('-inf')
        for i in arr:
            sumvalue+=i
            if sumvalue>maxvalue:
                maxvalue=sumvalue
            if sumvalue<0:
                sumvalue=0
        return maxvalue
        """
        :type nums: List[int]
        :rtype: int
        """
        