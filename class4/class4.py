'''
Binary Search: Repeatedly cut the search space in half until you find the answer

Conditions:
** The array is sorted **

704) Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
                0 1 2 3 4 5
Input: nums = [-1,0,3,5,9,12], target = 9
                      l   
                      r
                      m

                while l <= r or l < r
                1) (r + l) // 2 = 5 + 0 // 2 = 2.5 -> 2
                2) 
                nums[m] == target? 9 = 9, so return 4 
                3) update l to m + 1

Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
                l 
                m
            r
Output: -1
Explanation: 2 does not exist in nums so return -1
 

def binary_search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1

time complexity: o(log n)
space complexity: o(1)


35) Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
               0 1 2 3
Input: nums = [1,3,5,6], target = 2
                 l     
               r
               m 
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

def search_insert_pos(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return l

               0 1 2 3
Input: nums = [1,3,5,6], target = 6

** One comparison tells you which half must contain the answer **

162) Find Peak Element
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, 
return the index to any of the peaks. You may imagine that nums[-1] = nums[n] = -∞. In other words, 
an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

def peak_element(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[mid] < nums[mid+1]: # peak is on the right side b/c it's going up in value
            l = mid + 1
        else:
            r = mid
    
    return l


** There is a monotonic condition -> meaning once something becomes True (or False), it never changes back. **
Good for finding smallest answer that works

Monotonic Example:

A ride requires you to be at least 48 inches tall.
Participants: [40, 42, 46, 48, 50, 54]

0 40 inches x
1 42 inches x
2 46 inches x
3 48 inches =
4 50 inches =
5 54 inches =

Once you're tall enough, every taller height also qualifies.
False False False True True True -> Montonic condition
Binary Search can be used to find the first value that becomes True.


875) Koko eating bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23


def koko_brute_force(piles, h):
    pass
    


def koko_optimized(piles, h):
    pass


'''