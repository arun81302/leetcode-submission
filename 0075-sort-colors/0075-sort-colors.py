class Solution(object):
    def sortColors(self, arr):
        low=mid=0
        high=len(arr)-1
        while mid<=high:
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                mid+=1
                low+=1
            elif arr[mid]==1:
                arr[low],arr[mid]=arr[mid],arr[low]
                mid+=1
            elif arr[mid]==2:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
        return arr

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        