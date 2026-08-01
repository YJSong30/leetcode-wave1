'''
print(ord("b") - ord("a")) = 98 - 97 = 1


Two Pointers: use two or more indices that move through the array instead of using nested for loops

left = 0
right = len(nums) - 1

nums = [1, 2, 4, 7, 11]
        L            R

167) Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
                  l       r
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

def two_sum_sorted(self, nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        curr_sum = nums[l] + nums[r]
        if curr_sum == target:
            return [l+1, r+1]
        elif curr_sum > target:
            r -= 1
        else:
            l += 1
    
    return []


125) A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
                   ^
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

def isPalindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
    
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
    
    return True

t.c = o(n)
s.c = o(1)

283) Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
               ^
                 ^ 
            [1,3,12,0,0]
                 l
                      r 
            [1,3,12,0,0]
                 ^
                      ^ 
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

def zeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

t.c: o(n)
s.c: o(1)
'''