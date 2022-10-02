def pacific_ocean(matrix):
  pacific = len(matrix)*[len(matrix[0])]
  atlantic = len(matrix)*[len(matrix[0])]

  for col in range(len(matrix[0])):
    dfs(matrix, 0, col, min())


def dfs(grid,row,col,preVal,ocean):
  # check conditions
  if row < 0 or col < 0 or row > len(matrix)-1 or col > len(matrix[0]) - 1: # check coord is inbond
    return
  if matrix[row][col] < preVal:
    return
  if ocean[row][col] == 1: # check for visited
    return
  # Process cell
  ocean[row][col] = 1 # mark visited

  # call dfs
  dfs(matrix, row -1, col, matrix[row][col], ocean)
  dfs(matrix, row -1, col, matrix[row][col], ocean)
  dfs(matrix, row, col - 1, matrix[row][col], ocean)
  dfs(matrix, row, col+1, matrix[row][col], ocean)