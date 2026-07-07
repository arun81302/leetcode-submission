class Solution(object):
    def flipAndInvertImage(self, arr):
        def check(arr):
            i=0
            j=len(arr)-1
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            return arr
        for i in range(len(arr)):
            arr[i]=check(arr[i])
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j]==0:
                    arr[i][j]=1
                else:
                    arr[i][j]=0
        return arr
            
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        