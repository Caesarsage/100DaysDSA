# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in 
# non-decreasing order.

 
def sortedSquares(self, nums):
  """
  :type nums: List[int]
  :rtype: List[int]
  """
  sorted_arr = sorted([n**2 for n in nums])
  return sorted_arr