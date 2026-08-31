'''
1. What is a Stack?

A stack follows: LIFO = Last In, First Out

2. Stack in Python

You normally just use a list:

stack = []

# push
stack.append(5)
stack.append(10)
stack.append(20)

# look at top
print(stack[-1])    # 20

# pop
value = stack.pop() # 20

print(stack)
# [5, 10]

Important operations:

stack.append(x)  # push     O(1)
stack.pop()      # pop      O(1)
stack[-1]        # peek     O(1)
len(stack)       # size     O(1)

Don't do:

stack.pop(0)

That's removing from the front, and it's O(n).

3) When to use stacks
- When something from earlier needs to be rememebered, and the most recent thing is the first thing you need to deal with

20) Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''


'''
739) Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
                        0  1 2  3  4  5  6 7 8
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
'''