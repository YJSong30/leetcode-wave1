'''
Python syntax
Big O + Arrays
'''

# Python Syntax

'''
for loops:

for i in range(start, stop, step):
    do ...

for i in range(len(nums)): # 0 -> len(nums) - 1
    do ...

for num in nums:
    do...

indexing in an array/list:

        0 1 2 3 4
nums = [1,2,3,4,5]
nums[2] = 3

adding stuff to a list:
nums = []
for i in range(5):
    nums.append(i)

nums = [0,1,2,3,4]

'''

# Big O

'''

Time Complexity

nums = [1,2,3,4,5]
for i in range(nums):
    print(i)

nums = [1,2,3,4,5,6,7,8,9,10]
for i in range(nums):
    print(i)


Space Complexity

nums = []
for i in range(5):
    nums.append(i)

for i in range(10):
    nums.append(i)

    
'''


# Arrays

'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 
Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


Given an array of positive integers nums and an integer k, 
return the number of contiguous subarrays where the product 
of all the elements in the subarray is strictly less than k


Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8


Example 2:
Input: nums = [1, 2, 3], k = 5
Output: 4
'''
