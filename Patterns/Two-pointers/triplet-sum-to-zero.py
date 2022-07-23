# Problem Statement
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

def search_triplets(arr):
  arr.sort()
  triplets = []
  # TODO: Write your code here
  arr.sort()
  for i in range(0, len(arr)-2):
    if arr[i] == arr[i-1] and i > 0:
      continue

    left, right = i + 1, len(arr) - 1
    while left < right:
      threeSum = arr[i] + arr[left] + arr[right]
      if threeSum > 0:
        right -= 1
      elif threeSum < 0:
        left += 1
      else:
        triplets.append([arr[i], arr[left], arr[right]])
        left += 1
        right -= 1
        while left < right and arr[left] == arr[left - 1]:
          left += 1  # skip same element to avoid duplicate triplets
        while left < right and arr[right] == arr[right + 1]:
          right -= 1
  return triplets
