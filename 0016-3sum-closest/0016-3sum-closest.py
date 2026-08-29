class Solution(object):
    def threeSumClosest(self, arr, t):
        arr.sort()
        close=arr[0]+arr[1]+arr[2]
        for i in range(len(arr)-2):
            if arr[i]==arr[i-1] and i>0:
                continue
            a=i+1
            b=len(arr)-1
            while a<b:
                value=arr[i]+arr[a]+arr[b]
                if abs(t-value)<abs(t-close):
                    close=value
                if value==t:
                    return value
                if value<t:
                    a+=1
                else:
                    b-=1
        return close
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        