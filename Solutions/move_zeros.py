def move_zeros(nums):
  pointer = 0
  for r in range(len(nums)):
    if nums[r] != 0:
      nums[r], nums[pointer] = nums[pointer], nums[r]
      pointer -=1
  return nums