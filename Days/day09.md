# Other Array Questions

- [Other Array Questions](#other-array-questions)
  - [Questions](#questions)
  - [Solution thought flow](#solution-thought-flow)
    - [Q1 Height Checker](#q1-height-checker)
    - [Q2 Third Maximum Number](#q2-third-maximum-number)
    - [Q3 2D Array - DS](#q3-2d-array---ds)
    - [Q4 Arrays: Left Rotation](#q4-arrays-left-rotation)
    - [Q5 New Year Chaos](#q5-new-year-chaos)
    - [Q6 Minimum Swap 2](#q6-minimum-swap-2)
    - [Q7 Array Manipulaton](#q7-array-manipulaton)

## Questions

[Height Checker](../Solutions/height_checker.py)
[Third Maximum Number](../)
[2D Array - DS](../Solution/hourglass.py)
[Arrays: Left Rotation](../Solution/../Solutions/rotateLeft.py)
[New Year Chaos](../Solutions)
[Minimum Swap 2](../)
[Array Manipulation](../)

## Solution thought flow

### Q1 Height Checker

> A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
Return the number of indices where heights[i] != expected[i]

### Q2 Third Maximum Number
>Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number

### Q3 2D Array - DS

>[https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays]

```
// Example 1
// arr[i][j] =
// [
//   [ 1, 1, 1, 0, 0, 0 ],
//   [ 0, 1, 0, 0, 0, 0 ],
//   [ 1, 1, 1, 0, 0, 0 ],
//   [ 0, 0, 2, 4, 4, 0 ],
//   [ 0, 0, 0, 2, 0, 0 ],
//   [ 0, 0, 1, 2, 4, 0 ]
// ]
// an hourglass might look like
// 1 1 1
//   1 
// 1 1 1
// or
// arr[0][0], a[0][1], a[0][2]
//            a[1][1]
// arr[2][0], a[2][1], a[2][2]
// The sum of this first hourglass is 7

All hour glass combinations:

1 1 1     1 1 0     1 0 0     0 0 0
  1         0         0         0
1 1 1     1 1 0     1 0 0     0 0 0
 
0 1 0     1 0 0     0 0 0     0 0 0
  1         1         0         0
0 0 2     0 2 4     2 4 4     4 4 0
1 1 1     1 1 0     1 0 0     0 0 0
  0         2         4         4
0 0 0     0 0 2     0 2 0     2 0 0
0 0 2     0 2 4     2 4 4     4 4 0
  0         0         2         0
0 0 1     0 1 2     1 2 4     2 4 0

The sum of each hourglass from left to right, top to bottom:

7     4     2     0
4     8     10    8
3     6     7     6
3     9     19    14

The larges value of all the hourglasses:

If we do the same and replace the for index of arr[i][j] with our col variable.
1, 1, 1, 0, 0, 0     
0, 1, 0, 0, 0, 0     
1, 1, 1, 0, 0, 0     
0, 0, 2, 4, 4, 0     
0, 0, 0, 2, 0, 0     
0, 0, 1, 2, 4, 0
// row = 0 from our for loop
// col = 0 from our for loop
 
// First hourglass is
 
arr[row][col]         // 1 - top left
arr[row][col + 1]     // 1 - top middle
arr[row][col + 2]     // 1 - top right
arr[row + 1][col + 1] // 1 - middle middle
arr[row + 2][col]     // 1 - bottom left
arr[row + 2][col + 1] // 1 - bottom middle
arr[row + 2][col + 2] // 1 - bottom right

``
### Q4 Arrays: Left Rotation

>[https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays]

### Q5 New Year Chaos

>[https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays]

### Q6 Minimum Swap 2

>[https://www.hackerrank.com/challenges/minimum-swaps-2/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays]

### Q7 Array Manipulaton

>[https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays]