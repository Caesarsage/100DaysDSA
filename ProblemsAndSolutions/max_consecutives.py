# Maximum Consecutive Ones


# Given a binary array nums, return the maximum number of Subsecutive 1's in the array


# Understanding




def maxConsecutive(nums):
  count = maxCount = 0
        
  for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
    else:
      maxCount = max(count, maxCount)
      count = 0      
    return max(count, maxCount)

print(maxConsecutive([[1,1,0,1,1,1]]))