def minSwap(arr):
  count, i = 0, 0
  while i < len(arr):
    index = arr[i] - 1
    if arr[i] != arr[index]:
      arr[i], arr[index] = arr[index], arr[i]
      count +=1
    else:
      i +=1
  return count
