class Solution(object):
    def threeSum(self, arr):

        arr.sort()
        res=[]
        for i in range(len(arr)):

            if i>0 and arr[i]==arr[i-1]:
                continue
            target=-1*arr[i]
            a=i+1
            b=len(arr)-1
            while a<b:
                value=arr[a]+arr[b]
                if value==target:

                    res.append([arr[i],arr[a],arr[b]])
                    
                    a+=1
                    b-=1
                    one=arr[a]
                    two=arr[b]
                    while a<b and arr[a]==arr[a-1]:
                        
                        a+=1
                    while a<b and arr[b]==arr[b+1]:
                        
                        b-=1
                    
                elif value<target:
                    a+=1
                else:
                    b-=1
        return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        