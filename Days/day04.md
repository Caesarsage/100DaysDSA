# ARRAY

<!-- create table -->

Arrays are a simple data structure for storing lots of similar items. They exist in all programming languages, and are used as the basis for most other data structures. On their own, Arrays can be used to solve many interesting problems. Arrays come up very often in interview problems, and so being a guru with them is a must!

## Questions

- [Maximum Consecutive Ones](../Solutions/max_consecutives.py)
- [Find Number with even number of Digits](../Solutions/even_no_digit.py)
- [Squares of a sorted array](../Solutions/sorted_array.py)

### Solution thought flow

## Q1. Maximum Consecutive Ones

>Given a binary array nums, return the maximum number of Subsecutive 1's in the array

- set a variable to keep track of maximum ones and current ones.
- loop through each num in the array 
- for each number, if it is equal to 1
- increase current ones
- else, find maximum ones as max between itself and current ones and set to zero
  
## Q2. Find Number with even number of Digits

> Given an array nums of integers, return how many of them contain an even number of digits

- set a count variable
- loop through the array 
- since we are considering each digit but have an integer array, convert each num to a string
- check if the len of the new digit str(num) is divisible by 2
- increase the count and return after loops ends


### Q3. Squares of a sorted array

> Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 

- loop through the array
- square each number first
- then sort the array of squared.


###### I am  welcoming any more optimized solution you have, Make a PR
## we move

see you on <a href="./day05.md">Day 05</a>