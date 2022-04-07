def findNumbers(self, nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  count=0
  for num in nums:
      if len(str(num)) % 2 == 0:
          print(num)
          count +=1
  return count