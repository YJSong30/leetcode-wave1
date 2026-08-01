'''
706) Design Hashmap (no built in dict)

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def hash_func(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return

49) Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
                             ^
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

{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan","nat"],
    "abt": ["bat"],
}

def group_anagrams(self, strs):
    groups = defaultdict(list)

    for word in strs: # o(n)
        sorted_word_key = "".join(sorted(word)) # m log m
        groups[sorted_word_key].append(word)

    return list(groups.values())


# t.c: o(n * m log m)
# s.c: o(n * m)

n = number of words
m = average number of characters

"eate"
"atee"

counts = [0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] -> tuple(counts) -> (0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

{

     (0,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) : ["atee", "eate"]
}
def group_anagrams_optimized(strs):
    groups = defaultdict(list)

    for word in strs:
        counts = [0] * 26
        for char in word:
            index = ord(char) - ord("a")
            count[index] += 1
        key = tuple(counts)
        groups[key].append(word)
    
    return list(groups.values())

# time complexity: o(n * m)
# splace complexity: o(n * m)

560) Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

k = curr_sum - prev_sum
prev_sum = curr_sum - k

Example 2:
Input: nums = [1,2,3], k = 6
                     ^
               running_sum = 6
               6 - 3 = 3

{
    0: 1,
    1: 1,
    3: 1,
    6: 1
}

res = 2
Output: 2

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

prefix_sum + hashmap

[0,0,0]
 0 1 2

[0]
[0]
[0]

k = 0
3 subarrays equals k

sum(1,3)
sum between prefixes -> prefix_sum[3+1] - prefix_sum[1]

def subarray_sum(nums, k):
    res = 0
    curr_sum = 0
    seen = defaultdict(int)
    seen[0] = 1

    for i in range(len(nums)):
        curr_sum += nums[i]
        prev_sum = curr_sum - k

        if prev_sum in seen:
            res += seen[prev_sum]
        
        seen[curr_sum] += 1
    
    return res

t.c: o(n)
s.c: o(n)

'''