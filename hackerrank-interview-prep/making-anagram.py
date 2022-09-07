from turtle import st


from collections import Counter

def makingAnagram(a: str,b: str) :
  map = Counter(a)

  for ch in b:
    if ch in map:
      map[ch] -=1
    else:
      map[ch] = -1
  
  total_values = sum(abs(value) for value in map.values())
  return total_values
