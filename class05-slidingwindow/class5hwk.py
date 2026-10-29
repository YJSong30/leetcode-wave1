'''
1) Longest Substring With At Most Two Distinct Characters
Given a string s, return the length of the longest substring containing at most two distinct characters.
- Use the sliding window technique.
- Target O(n) time.

Example 1:
Input:  s = "eceba"
             l
             r

             r - l + 1 -> length of substring

        s_frequency = {
            b: 1
            a: 1
        }

        longest_substring = float('-inf')
        longest_substring = max(longest_substring, r - l + 1)

        return longest_substring
Output: 3

Example 2:
Input:  s = "ccaabbb"
               ^
             ccaa -> 4
             aabbb -> 5
Output: 5

Constraints:
- 1 <= s.length <= 10^5


from collections import defaultdict

def longest_distinct_char(s):
    l = 0
    s_freq = defaultdict(int)
    longest_substring_len = float('-inf')

    for r in range(len(s)):
        s_freq[s[r]] += 1

        # check if breaks condition -> update window (l pointer)
        while len(s_freq) > 2:
            l_char = s[l]
            s_freq[l_char] -= 1
            if s_freq[l_char] == 0:
                del s_freq[l_char]

            l += 1
        
        longest_substring_len = max(longest_substring_len, r - l + 1)
        
    return longest_substring_len

print(longest_distinct_char("eceba")) # 3
print(longest_distinct_char("ccaabbb")) # 5


2) Longest Subarray With No Repeated Values
Given an integer array nums, return the length of the longest contiguous subarray containing no duplicate values.

- Use the sliding window technique.
- Target O(n) time

Example 1:
Input: nums = [1,2,3,1,2]
                   l
                       r
               {3,1,2}
               longest_len = 3
Output: 3

Example 2:
Input: nums = [4,2,4,5,6]
                 l
                       r
               {2,4,5,6}
               longest_len = 4
Output: 4

Constraints:
- 1 <= nums.length <= 10^5

use memory -> set for checking duplicates

def longest_subarray_len(nums):
    l = 0
    seen = set()
    longest_len = float('-inf')

    for r in range(len(nums)):
    
        # check break condition
        while nums[r] in seen:
            seen.remove(nums[l])
            l += 1

        seen.add(nums[r])
        longest_len = max(longest_len, r - l + 1)
    
    return longest_len

print(longest_subarray_len([1,2,3,1,2])) # 3
print(longest_subarray_len([4,2,4,5,6])) # 4

'''
