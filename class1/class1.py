'''
Python syntax
Big O + Arrays
'''

# Python Syntax for Arrays

'''
** for loops **

for i in range(start, stop, step):
    ...

for i in range(len(nums)): # 0 -> len(nums) - 1
    ...

for num in nums:
    ...

** nested for loops **

for i in range(len(nums)):
    for j in range(len(nums)):
        ...

** indexing in a list **

        0 1 2 3 4
nums = [1,2,3,4,5]
nums[2] = 3

** adding stuff to a list **

nums = []
for i in range(5):
    nums.append(i)

nums = [0,1,2,3,4]
'''

# Big O

'''

** Time Complexity **

nums = [1,2,3,4,5]

for i in range(len(nums)): # execute 5 times
    print(i)

nums = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(nums)): # execute 10 times
    print(i)

n = length of input
o(n)


** Space Complexity **

k = 5
nums = []
for i in range(k):
    nums.append(i)

nums = [0,1,2,3,4]

k = 10
for i in range(k):
    nums.append(i)

nums = [0,1,2,3,4,5,6,7,8,9]

o(n)

'''


# Arrays

'''
** Two Sum **

1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
               0 1 2
Input: nums = [2,7,11,15,...40,50], target = 90
               i 
                 j

Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

def two_sum(nums, target):
    for i in range(len(nums)): # o(n)
        for j in range(i+1, len(nums)): # o(n)
            if nums[i] + nums[j] == target: # o(1)
                return [i,j] # o(1)

worst case scenario: 
time complexity: o(n^2) -> o(n)
space complexity: o(1) -> increase memory complexity


** Nested for loop **

713: Given an array of positive integers nums and an integer k, return the number of contiguous subarrays where the product 
of all the elements in the subarray is strictly less than k

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
                   i
                   j

Output: 8

[10] = 10
[10,5] = 50
[5] = 5
[5,2] = 10
[5,2,6] = 60
[2] = 2
[2,6] = 12
[6] = 6

Example 2:
Input: nums = [1, 2, 3], k = 5
Output: 4

- keep track of how many subarrays you counted that fit the condition strictly less than k -> count = 0
- variable to reset the product = 1

def product_arrays(nums, k):
    count = 0 # o(1)

    for i in range(len(nums)): # o(n)
        product = 1 # o(1)
        for j in range(i, len(nums)): # o(n)
            product *= nums[j] # o(1) 
            if product < k: # o(1)
                count += 1 # o(1) 
            else: # o(1)
                break # o(1)
                
    return count # o(1)

time complexity: o(n) * n(n) = o(n^2)
space complexity: o(1)


** Prefix Sums **

        0 1 2 3 4
nums = [1,2,3,4,5]

sum(1,3) = 9

def prefix_sum_brute_force(nums, l, r): # o(n)
    total = 0
    for i in range(l, r + 1):
        total += nums[i]
    return total

prefix_sum_brute_force(nums, 1, 3):


sum(1,3) = 1 + 2 + 3 = 6
sum(2,4) = 2 + 3 + 4 = 9

query this k times where k represents a new number every time
k = 50

time complexity: o(n * k)


              0.  1. 2 3 4.  5
prefix_sum = [0, 1, 3, 6, 10, 15]

    l r
sum(1,3) = prefix_sum[r + 1] - prefix_sum[l] = prefix_sum[4] - prefix_sum[1] = 10 - 1 = 9 # o(1)
sum(2,4) = prefix_sum[5] - prefix_sum[2] = 15 - 3 = 12 # o(1)

# time complexity: o(n * k) -> o(n)
# space complexity: o(n)

class PrefixSum:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]
    
    def prefix_sum_query(self, left, right): 
        return self.prefix[right + 1] - self.prefix[left] # o(1)


'''
