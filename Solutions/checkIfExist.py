# class Solution(object):
def checkIfExist(self, arr):
  """
  :type arr: List[int]
  :rtype: bool
  """
  hashSet= set()
  for i in range(len(arr)):
    if arr[i]*2 in hashSet or (arr[i]%2==0 and arr[i]//2 in hashSet):
      return True
    hashSet.add(arr[i])
    
  return False