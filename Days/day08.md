## Array In place

In programming interviews, the interviewer often expects you to minimise the time and space complexity of your implementation. In-place Array operations help to reduce space complexity, and so are a class of techniques that pretty much everybody encounters regularly in interviews.

## Questions

[Replace Elements with Greatest Element on Right Side](../Solutions/replace_element_gretest_rhs.py)
[Move Zeroes](../Solutions/move_zeros.py)
[Sort By Parity](../Solutions/sort_by_parity.py)

## Solution thought flow
Q1
>Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

- we are starting from back to end
- initialize a max variable to a negative 1, i.e  max variable represent what on the right
- iterate from back to end
- each round, we set the array value to the max variable and update the max variable to the  maximum between it current state and current value

Q2.

>Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

- This case we iterate from start to end
- initialize a pointer to 0
- iterate through the array length
- if each num is not equal to zero, we need to perform a swap between the current number, pointer number position and the pointer number location, current number respectively then also reduce the pointer by 1
- return the nums at the end of the loop


Q3
>Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.


- Using two pointer, one at the beginning of the arr and the other at the end.
- while the beg is less than or equal to the end.
- we check if the current beginning number is divisible by 2, hence increase the beginning number by 1
- else, we swap the beg num and end num with end number and beg num respectively
- we can return the arr num after while loop