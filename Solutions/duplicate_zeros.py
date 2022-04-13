def duplicateZeros(self, arr):
  """
  :type arr: List[int]
  :rtype: None Do not return anything, modify arr in-place instead.
  """
  i=0
  while i<len(arr):
      if arr[i] == 0:
          arr.insert(i+1,0)
          del arr[-1]
          i+=2
      else:
          i+=1
  return arr