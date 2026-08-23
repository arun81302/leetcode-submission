class Solution(object):
    def majorityElement(self, arr):
        cand=0
        count=0
        for i in arr:
            if count==0:
                cand=i
            if i==cand:
                count+=1
            else:
                count-=1
        return cand
        """
        :type nums: List[int]
        :rtype: int
        """
        