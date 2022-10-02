class Solution(object):
  def replaceElements(self, arr):
      """
      :type arr: List[int]
      :rtype: List[int]
      """
      max_last = -1
      for j in range(len(arr)-1, -1, -1):
          arr[j], max_last = max_last, max(max_last, arr[j])
      return arr