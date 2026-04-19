class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # Stores unique characters in the current window
        l = 0            # Left pointer of the sliding window
        res = 0          # Tracks the maximum length found

        for r in range(len(s)):  # Right pointer of the sliding window
            while s[r] in charSet:
                # If duplicate found, shrink window from the left
                charSet.remove(s[l])
                l += 1
            # Add current character to the set and update result
            charSet.add(s[r])
            res = max(res, r - l + 1)  # Update max length if longer window found
        return res
