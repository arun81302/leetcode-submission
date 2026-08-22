class Solution(object):
    def singleNumber(self, arr):
        value=0
        for i in arr:
            value^=i
        return value
        """
        :type nums: List[int]
        :rtype: int
        """
        