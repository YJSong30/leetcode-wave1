'''
75) Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function. -> come up with a solution that's faster than time compleixty o(n log n)

- dutch national flag algorithm
- one pass
- intuition: increment c pointer (the scanner pointer), find a 0 or 1, then swap if it's a 0 to the left side
                    - if it's a 2, swap -> decrement r pointer but don't increment the scanner

Example 1:
Input: nums = [2,0,2,1,1,0] -> [0,0,1,1,2,2]
               l         r        l   r
               c                       c
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1] -> [1,0,2] -> [0,1,2]
               l   r.     l r          r
                c           c          l
                                         c 

Output: [0,1,2]

Example 3:
Input: nums = [1,2,0] -> [1,0,2] -> [0,1,2]
               l   r      l r          l
                                       r
                                          c
                 c          c

Output: [0,1,2]

def sort_colors(nums):
    left = 0
    right = len(nums) - 1
    curr = 0

    while curr <= right:
        if nums[curr] == 2:
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1
        elif nums[curr] == 0:
            nums[curr], nums[left] = nums[left], nums[curr]
            left += 1
            curr += 1
        else:
            curr += 1

t.c: o(n)
s.c: o(1)


11) You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
 
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

def max_container(height):
    nums = height
    max_area = float('-inf')
    left = 0
    right = len(nums) - 1

    while left < right:
        current_area = (r - l) * min(nums[left], nums[right])
        max_area = max(max_area, current_area)

        if nums[left] > nums[right]:
            r -= 1
        else:
            l += 1
    
    return max_area

t.c: o(n)
s.c: o(1)


15) Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]
                                             
                                    nums[i] + nums[l] + nums[r] == 0?
                                        - if true, append to res = [[-1,-1,2],[-1,0,1]]
                                        - if false
                                            - sum > 0 -> smaller sum move right pointer down
                                            - sum < 0 -> bigger sum move left pointer up
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

def 3sum(nums):
    nums.sort() # o(n log n)
    res = []

    for i in range(len(nums) - 2):
    
        nums[i] > 0:
            break
        
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l = i + 1
        r = len(nums) - 1

        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum == 0:
                res.append([nums[i], nums[l], nums[r]])

                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1
                
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            
            elif curr_sum > 0:
                r -= 1

                # while l < r and nums[r] == nums[r+1]:
                #     r -= 1
            
            else:
                l += 1

                # while l < r and nums[l] == nums[l-1]:
                #     l += 1
    
    return res

t.c: o(n^2)
s.c: o(k) where k represents the number of distinct triplets

'''