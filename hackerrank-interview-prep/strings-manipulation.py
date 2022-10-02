def stringManipulation(s):
  count = 0
  for j in range(1, len(s)):
    if(s[j] == s[j-1]):
      count +=1
  return count