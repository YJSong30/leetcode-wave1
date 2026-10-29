from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = Counter(t)
        s_freq = defaultdict(int)
        l = 0
        currently_have_freq = 0
        need_freq = len(t_freq)

        # smallest_substr = ""
        smallest_substring_len = float('inf')
        l_pointer = 0
        r_pointer = 0

        for r in range(len(s)):
            char = s[r]
            s_freq[char] += 1
            
            if char in t_freq and s_freq[char] == t_freq[char]:
                currently_have_freq += 1

            while currently_have_freq == need_freq:
                curr_length = r - l + 1
                if curr_length < smallest_substring_len:
                    # curr_str = s[l:r+1]
                    l_pointer = l
                    r_pointer = r
                    smallest_substring_len = min(smallest_substring_len, curr_length)
                
                # break window here to get smaller substring
                # 1) decrease frequency
                l_char = s[l]
                s_freq[l_char] -= 1
                # 2) check if freq == 0 then del
                if s_freq[l_char] == 0:
                    del s_freq[l_char]
                
                # 3) if the frequency of that char decreases (i.e less than char in t_freq, then decrement currently_have_freq)
                if l_char in t_freq and s_freq[l_char] < t_freq[l_char]:
                    currently_have_freq -= 1

                # 4) increment l pointer
                l += 1

        if smallest_substring_len == float('inf'):
            return ""
            
        return s[l_pointer:r_pointer+1]

# curr_str = "bob"
#                ^
# curr_str += "a"

# curr_str = ""
# curr_str = "boba"