class Solution(object):
    def threeSum(self, arr):
        arr.sort()
        ans=[]
        res=[]
        for i in range(len(arr)):
            j=i+1
            k=len(arr)-1
            while j<k:
                value=arr[i]+arr[j]+arr[k]
                if value==0:
                    res.append([arr[i],arr[j],arr[k]])
                if value<0:
                    j+=1
                else:
                    k-=1
        res.sort()
        if len(res)==0:
            return res
        ans=[res[0]]
        for i in range(1,len(res)):
            if res[i]!=ans[-1]:
                ans.append(res[i])
        return ans
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        