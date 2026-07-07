class Solution(object):
    def sumAndMultiply(self, n):
        if n==0:
            return 0
        sumvalue=0
        arr=[int(i) for i in str(n)]
        res=""
        for i in arr:
            if i!=0:
                sumvalue+=i
                res+=str(i)
        res=int(res)
        return res*sumvalue
        """
        :type n: int
        :rtype: int
        """
        