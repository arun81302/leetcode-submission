class Solution(object):
    def findClosestNumber(self, arr):
        value = arr[0]

        for i in arr:
            if abs(i) < abs(value):
                value = i
            elif abs(i) == abs(value) and i > value:
                value = i

        return value
        """
        :type nums: List[int]
        :rtype: int
        """