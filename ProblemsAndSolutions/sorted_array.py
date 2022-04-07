def sortedSquares(self, nums):
  """
  :type nums: List[int]
  :rtype: List[int]
  """
  sorted_arr = sorted([n**2 for n in nums])
  return sorted_arr