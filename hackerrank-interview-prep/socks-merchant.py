# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example


# There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is .
from collections import Counter

def sockMerchant(n, arr):
  count = Counter(arr)  # Create a dictlike key pair of value count

  onlyCounterValue = count.values()
  pairs = 0

  for elem in onlyCounterValue:
    pairs = pairs + elem //2
  return pairs
