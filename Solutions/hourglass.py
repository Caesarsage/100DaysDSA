def hourglassSum(arr):
    # Write your code here
    max_sum = -99999999999
    for row in range(4):
        arr_sum=0
        for col in range(4):
            arr_sum =arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1]+ arr[row+2][col] +arr[row+2][col+1]  + arr[row+2][col+2]
            max_sum = max(max_sum, arr_sum)
    return max_sum
        