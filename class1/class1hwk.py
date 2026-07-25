'''
1) You are given a binary array nums (only 0s and 1s). 
Return the length of the longest contiguous subarray that contains an equal number of 0s and 1s.

Example 1:
Input: nums = [0, 1, 0, 1, 1]
               i
                  j
Output: 4

Example 2:
Input: nums = [0, 0, 1, 0, 1, 1]
Output: 6

def contiguous_subarray(nums):
    max_len = 0
    for i in range(len(nums)):
        zeros = 0
        ones = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                max_len = max(max_len, j - i + 1)
    return max_len

t.c: o(n^2)
s.c: o(1)


2) Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:
Input: nums = [100,4,200,1,3,2]
               num 
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

def longest_consecutive(nums):
    longest = 0
    for num in nums: # o(n)
        current_num = num
        length = 1
        while current_num + 1 in nums:
            current_num += 1
            length += 1
        
        longest = max(longest, length)
    
    return longest

t.c: o(n^3)
s.c: o(1)


3) Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
 
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

def min_len(nums):
    min_length = float('inf')
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total >= target:
                min_length = min(min_length, j - i + 1)
    
    if min_length == float('inf'):
        return 0
    
    return min_length

t.c: o(n^2)
s.c: o(1)
'''