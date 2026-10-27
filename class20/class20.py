'''
Backtracking

--------------------------------------------------
Backtracking is an algorithm that explores different
possible solutions by making and undoing choices.

Usually implemented using recursive DFS.

Core pattern:
1. Choose -> Add a choice to the current path.
2. Explore -> Recursively try the next choices.
3. Undo -> Remove the choice (backtrack).

Common keywords:
- Find all combinations
- Find all permutations
- Find all subsets
- Generate all possible solutions
- Find all valid paths

Key concepts:
- path: Stores the current choices.
- res: Stores completed solutions.
- append(): Make a choice.
- pop(): Undo the choice.
- Base case: Determine when a solution is complete.

Backtracking often has exponential or factorial
time complexity because it explores many possibilities.

78) Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
 
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(cur_list, i):
            # base case
            if i == len(nums):
                res.append(cur_list[:])
                return
            
            # work
            # take
            cur_list.append(nums[i])
            dfs(cur_list, i+1)
            cur_list.pop()

            # skip  
            dfs(cur_list, i+1)

        dfs([], 0)
        return res
        

39) Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        nums = candidates
        res = []

        def dfs(cur_list, i, cur_sum):
            if cur_sum == target:
                res.append(cur_list[:])
                return
            
            if cur_sum > target or i == len(nums):
                return

            # work
            # take
            cur_list.append(nums[i])
            dfs(cur_list, i, cur_sum + nums[i])
            cur_list.pop() 

            # skip
            dfs(cur_list, i + 1, cur_sum)

        dfs([], 0, 0)
        return res
 

'''

