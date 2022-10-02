/*
1. Two Sum - https://leetcode.com/problems/two-sum/
*/

// Approach 1. O(n * n)
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++)
        for (let j = 0; j < nums.length; j++) 
            if (nums[i] + nums[j] === target && i !== j)
                return [i, j];
}; 

// Approach 2. O(n)
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) { 
         let indexOfDiff = nums.indexOf(target - nums[i]);
         if (indexOfDiff !== -1 && indexOfDiff !== i) return [i, indexOfDiff]; 
     } 
};