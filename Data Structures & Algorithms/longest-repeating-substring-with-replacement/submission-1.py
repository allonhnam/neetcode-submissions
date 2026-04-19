class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}      # stores frequency of each character in current window
        res = 0         # stores the longest valid window found
        l = 0           # left pointer of sliding window
        maxf = 0        # highest frequency of any single character in window

        # XYYX

        # Sliding window: r expands to the right
        for r in range(len(s)):

            # Add current character to the window
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update max frequency in this window
            maxf = max(maxf, count[s[r]])

            # If more than k replacements are needed,
            # shrink window from the left
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1   # remove left character
                l += 1            # move left pointer

            # Update result with current valid window size
            res = max(res, r - l + 1)

        return res
