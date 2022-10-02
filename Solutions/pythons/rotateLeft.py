def rotLeft(a, d):
  # Write your code here
  if len(a) <= 1:
    return
  if d < 0:
    return
  d = d % len(a)
  a[:] = a[d:] + a[:d]
  return a
