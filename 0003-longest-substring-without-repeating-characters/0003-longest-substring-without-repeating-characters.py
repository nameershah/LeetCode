class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Tracks { character: most_recent_index }
        left = 0
        res = 0
        
        for right, char in enumerate(s):
            # If the character is in our current window, jump 'left' past it
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            char_map[char] = right
            res = max(res, right - left + 1)
            
        return res
