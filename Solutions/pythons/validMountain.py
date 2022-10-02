class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        begining = 0
        end = n-1
        while begining != n-1 and arr[begining+1]> arr[begining]:
            begining +=1
        while end !=0 and arr[end-1]>arr[end]:
            end-=1
        if begining == end and end != n-1 and begining !=0:
            return True