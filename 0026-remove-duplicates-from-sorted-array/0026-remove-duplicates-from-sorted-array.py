class Solution(object):
    def removeDuplicates(self, arr):
        count=1
        i=0
        for j in range(1,len(arr)):
            if arr[j]!=arr[i]:
                i+=1
                arr[i]=arr[j]
                count+=1
        return count

        """
        :type nums: List[int]
        :rtype: int
        """
        