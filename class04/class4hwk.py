'''
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
    for i in range(1, max(piles) + 1):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / i)
                # pile / i (speed) = banana / (bananas/hrs) = hrs
                print(hours)
                
            if hours <= h:
                return i

# t.c: o(m * n) m = number of piles, n = max speed
# s.c: o(1)

def koko_optimized(piles, h):
    l = 0
    r = max(piles)
    res = max(piles)

    while l <= r:
        hours = 0
        mid = (l + r) // 2 # speed

        for pile in piles:
            hours += math.ceil(pile / mid)
        
        if hours <= h:
            res = min(res, mid)
            r = mid - 1
        else:
            l = mid + 1
    
    return res

# t.c: o(m log n) where m = number of piles, n = max speed
# s.c: o(1)

'''