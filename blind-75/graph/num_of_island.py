
def num_of_island(grid):
  count = 0
  row, col = len(grid), len(grid[0])
  for i in range(row):
    for j in range(col):
      if grid[i][j] == "1":
        num_of_island_dp(grid, i, j)
        count +=1
  return count



def num_of_island_dp (grid, row, col):
  # check for conditions
  if (row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1):
    return
  if grid[row][col] == "0": # if cell is 0.
    return
  
  # process cell
  grid[row][col] = 0 # zero out the cell

  # call dfs
  num_of_island_dp(grid, row, col - 1)
  num_of_island_dp(grid, row, col +1)
  num_of_island_dp(grid, row -1 , col)
  num_of_island_dp(grid, row+1, col)
