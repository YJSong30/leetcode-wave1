'''
Hashmap & Set

Hash map (dictionary): stores key-value pairs.
- lookup, insert, delete o(1)

Set: like hashmap but only stores keys (no values)
- useful for checking membership or removing duplicates in o(1)

Python syntax:

** Hashmap **

hashmap = {}
hashmap = dict()

hashmap["bob"] = 2 -> { "bob": 2 }
hashmap["bob"] += 1 -> { "bob": 3 }
"bob" in hashmap -> True (o(1) lookup)

hashmap = {"bob" : 1, "alice": 2, "james": 3}

hashmap.get("bob", 0) + 1 -> returns 3, or 0 if "bob" isn't a key
hashmap["bob"] = hashmap.get("bob, 0) + 1

del hashmap["bob"] -> {}
hashmap.keys() -> returns all keys
hashmap.values() -> returns all values
hashmap.items() -> all (key, value) pairs. useful for looping

for key, value in hashmap.items():
    print(key, value)

"bob" 1
"alice" 2
"james" 3

from collections import defaultdict

myHashmap = defaultdict(int)

{ "alice": 1 }

myHashmap["alice"] += 1 -> {"alice": 1}

myHashmap = defaultdict(list)

{ alice: [1] }

myHashmap["alice"].append(1) -> { "alice" : [1] }

** Set **

mySet = set()

mySet.add("bob") -> {"bob"}
mySet.add("bob") -> {"bob"}
bob in mySet -> True (lookup o(1))
mySet.remove("bob") -> {}

important: can only store immutable things for keys: strings, tuples, etc.

'''

# Hashmap/Set

'''

2260. You are given an integer array cards where cards[i] represents the value of the ith card. 
A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. 
If it is impossible to have matching cards, return -1.

Example 1:
                0 1 2 3 4 5
Input: cards = [3,4,2,3,4,3] 
                      i   
            {
                card: index,
                3: 0,
            }
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. 
Note that picking up the cards [4,2,3,4] is also optimal.

brute force:
- use two for loops to find subarrays. check if i == j if so get distance j - i + 1 and update min length variable
- t.c: o(n^2)
- s.c: o(1)

optimized:
- use hashmap to store the number and the index

Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
    
def min_cards(cards):
    seen = {} # number: index
    min_len = float('inf')

    for i in range(len(cards)):
        card = cards[i] # 3
        if card in seen:
            length = i - seen[card] + 1 -> length = 3 - seen[3] + 1 = 3 - 0 + 1
            min_len = min(min_len, length)
        seen[card] = i

    if min_len == float('inf'):
        return -1
    
    return min_len

- t.c: o(n)
- s.c: o(n)

49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]


Top K frequent elements

347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


{
    1: 3,
    2: 2,
    3: 1

}


Example 2:
Input: nums = [1], k = 1

Output: [1]
Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]


[(3,1), (2,2), (1,3)] -> sort
'''