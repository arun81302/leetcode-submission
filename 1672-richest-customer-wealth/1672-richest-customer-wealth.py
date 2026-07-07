class Solution(object):
    def maximumWealth(self, arr):
        maxsum=float('-inf')
        for i in range(len(arr)):
            sumvalue=0
            for j in range(len(arr[0])):
                sumvalue+=arr[i][j]
            maxsum=max(maxsum,sumvalue)
        return maxsum

        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        