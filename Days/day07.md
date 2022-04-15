## Array operations

- [Inserting](day05.md)
- [Deleting](day06.md)
- [Searching](day07.md)

There's more than one way of searching an Array, but for now, we're going to focus on the simplest way. Searching means to find an occurrence of a particular element in the Array and return its position. We might need to search an Array to find out whether or not an element is present in the Array. We might also want to search an Array that is arranged in a specific fashion to determine which index to insert a new element at.

If we know the index in the Array that may contain the element we're looking for, then the search becomes a constant time operation—we simply go to the given index and check whether or not the element is there.

- Linear Search
- Binary Search

## Linear Search

If the index is not known, which is the case most of the time, then we can check every element in the Array. We continue checking elements until we find the element we're looking for, or we reach the end of the Array. This technique for finding an element by checking through all elements one by one is known as the linear search algorithm. In the worst case, a linear search ends up checking the entire Array. Therefore, the time complexity for a linear search is O(N).

## Binary Search

There is another way of searching an Array. If the elements in the Array are in sorted order, then we can use binary search. Binary search is where we repeatedly look at the middle element in the Array, and determine whether the element we're looking for must be to the left, or to the right. Each time we do this, we're able to halve the number of elements we still need to search, making binary search a lot faster than linear search!

The downside of binary search though is that it only works if the data is sorted. If we only need to perform a single search, then it's faster to just do a linear search, as it takes longer to sort than to linear search. If we're going to be performing a lot of searches, it is often worth sorting the data first so that we can use binary search for the repeated searches.

## Questions

- [check if N and its double exist](../Solutions/checkIfExist.py)
- [valid mountain array](../Solutions/validMountain.py)

## Solution thought flow

> Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 *M).
More formally check if there exists two indices i and j such that :
>i != j
0 <= i, j < arr.length
arr[i] == 2* arr[j]

- Using hashSet, iterate through the arr
- check if 2 times arr value is in the hashSet or if the value is divisible by 2 (arr%2== 0 and arr//2 in the hashSet) and return True. That is you have found the double
- else add the number to the hashSet
- after the loop and no match is found, return False

Q2.
>Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

- Move from left of the arr to the right where possible it's increasing
- Move from end to left until our data is decreasing
- if we meet somewhere in the middle point which is neighbor 0 nor n-1, it means that we found our mountain, in other case array is not
- set two variables, start and end
- while start is not equal to the length of the array minus one and next number in the array is greater than the current start.
- increase the start by one
- Again for the end, while the end is not equal to zero and the next value from back(end-1) is greater than the  current end value
- decrease the end value by 1
- return the start equal to end and end end not equal to len of arr minus one and start not equal to zero. True return if yes

###### I am  welcoming any more optimized solution you have,Make a PR

# we move

see you on <a href="./day08.md">Day 08</a>
