def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n+2)

    # perform query operation
    for a, b, k in queries:
        arr[a] += k
        arr[b+1] -= k # balance the arr
        # print(arr)
        # find max element from the array
    maxnum = temp = 0
    for val in arr:
        temp += val
        maxnum = max(maxnum, temp)

    return maxnum
