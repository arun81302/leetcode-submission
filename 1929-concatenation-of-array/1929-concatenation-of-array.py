class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        res=[0]*(2*n)
        for i in range(n):
            res[i]=nums[i]
            res[n+i]=nums[i]
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        