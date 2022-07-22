# Quadruple Sum to Target(medium)
# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

# Example 1:

# Input: [4, 1, 2, -1, 1, -3], target = 1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.
# Example 2:

# Input: [2, 0, -1, 1, -2, 2], target = 2
# Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
# Explanation: Both the quadruplets add up to the target.
# Solution
# This problem follows the Two Pointers pattern and shares similarities with Triplet Sum to Zero.

# We can follow a similar approach to iterate through the array, taking one number at a time. At every step during the iteration, we will search for the quadruplets similar to Triplet Sum to Zero whose sum is equal to the given target.

def search_quadruplets(arr, target):
  arr.sort()
  quadruplets = []
  for i in range(0, len(arr)-3):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    for j in range(0, len(arr)-2):
      if j > 0 and arr[j] == arr[j-1]:
        continue
      
      left = j + 1
      right = len(arr) - 1
      while left < right:
        quad_sum = arr[i] + arr[j] + arr[left] + arr[right]
        if quad_sum == target:
          quadruplets.append([
            arr[i], arr[j], arr[left], arr[right]
          ])
          left += 1
          right -= 1
          
          while left < right and arr[left] == arr[left-1]:
            left += 1 
          while left < right and arr[right] == arr[right+1]:
            right -= 1
        elif quad_sum < target:
          left += 1
        else:
          right -= 1