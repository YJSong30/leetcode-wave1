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
303. Range Sum Query - Immutable

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
