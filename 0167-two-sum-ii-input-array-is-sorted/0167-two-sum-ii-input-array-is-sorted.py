class Solution(object):
    def twoSum(self, arr, t):
        sumvalue=0
        i=0
        j=len(arr)-1
        while i<j:
            sumvalue=arr[i]+arr[j]
            if sumvalue==t:
                return [i+1,j+1]
            elif sumvalue>t:
                j-=1
            else:
                i+=1
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        