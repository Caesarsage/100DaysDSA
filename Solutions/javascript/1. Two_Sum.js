/*
1. Two Sum - https://leetcode.com/problems/two-sum/
*/

// Approach 1.
// Time Complexity - O(n * n), Space Complexity - O(1)
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++)
        for (let j = 0; j < nums.length; j++) 
            if (nums[i] + nums[j] === target && i !== j)
                return [i, j];
}; 

// Approach 2.
// Time Complexity - O(n ), Space Complexity - O(1)
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) { 
         let indexOfDiff = nums.indexOf(target - nums[i]);
         if (indexOfDiff !== -1 && indexOfDiff !== i) return [i, indexOfDiff]; 
     } 
};

/*  Hashmap Solution
    Time Complexity - O(n)
    Space Complexity - O(n)
*/
var twoSum = function(nums, target) {
    // edge case for empty array
    if (!nums) return []

    let map = new Map()

    for (let i = 0; i < nums.length; i++) {
        if(map.has(target - nums[i])){
            return [map.get(target - nums[i]), i ]
        }else{
            map.set(nums[i], i)
        }   
    }

    return []
};
