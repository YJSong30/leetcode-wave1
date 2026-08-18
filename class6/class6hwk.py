'''
424. Longest Repeating Character Replacement
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

from collections import defaultdict
def longest_char_replace(s, k):
    s_freq = defaultdict(int)
    l = 0
    longest_len = float('-inf')

    for r in range(len(s)):
        char = s[r]
        s_freq[char] += 1

        # break condition
        while (r - l + 1) - max(s_freq.values()) > k:
            s_freq[s[l]] -= 1
            l += 1

        longest_len = max(longest_len, r - l + 1)
    
    return longest_len

def longest_char_replace_optimized(s, k):
    s_freq = defaultdict(int)
    l = 0
    max_freq = 0
    longest_len = float('-inf')

    for r in range(len(s)):
        char = s[r]
        s_freq[char] += 1

        max_freq = max(max_freq, s_freq[char])

        # break condition
        while (r - l + 1) - max_freq > k:
            s_freq[s[l]] -= 1
            l += 1

        longest_len = max(longest_len, r - l + 1)
    
    return longest_len

time complexity: o(n)
space complexity: o(26) -> o(1) 

567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

def permutation_str(s1, s2):
    if len(s1) > len(s2):
            return False
    
    s1_count = [0] * 26
    s2_count = [0] * 26

    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1
    
    if s1_count == s2_count:
        return True

    l = 0

    for r in range(len(s1), len(s2)):
        s2_count[ord(s2[l]) - ord('a')] -= 1
        l += 1

        s2_count[ord(s2[r]) - ord('a')] += 1

        if s1_count == s2_count:
            return True
    
    return False

hashmap verison:

    s1_freq = { a:1,
                b:1 }

    s2_freq = {  b:1
                 d: 1 }

    if s1_freq == s2_freq: return True
'''