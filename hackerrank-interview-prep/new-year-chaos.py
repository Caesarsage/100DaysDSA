def minBribe(q):
  swapCount = 0

  for i in range(len(q) - 1, 0, -1):
    if (q[i] != i + 1):  # filter case, only when there is a bribe
      if q[i - 1] == i + 1:
        swapCount += 1
        swap(q, i, i-1)
      elif q[i-2] == i + 1:
        swapCount += 2
        swap(q, i - 2, i - 1)
        swap(q, i - 1, i)
      else:
        print('Too Chaotic')
        return 'Too chaotic'
  print(swapCount)


def swap(q, i, j):
  q[i], q[j] = q[j], q[i]
