class Solution(object):
    def runningSum(self, nums):
        sumvalue=0
        for i in range(len(nums)):
            sumvalue+=nums[i]
            nums[i]=sumvalue
        return nums

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        