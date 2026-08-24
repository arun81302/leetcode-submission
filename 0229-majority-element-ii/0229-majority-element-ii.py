class Solution(object):
    def majorityElement(self, arr):
        value=len(arr)//3
        seen={}
        for i in arr:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        res=[]
        for key,values in seen.items():
            if values>value:
                res.append(key)
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        