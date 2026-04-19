class Solution:
    def generateParenthesis(self, n):
        res = [[] for _ in range(n+1)]  # res[k] will store all valid combinations of k pairs
        res[0] = [""]  # Base case: 0 pairs → empty string

        for k in range(1, n + 1):  # Build combinations for 1 to n pairs
            for i in range(k):
                # For each split: i pairs inside the current '()' and (k-i-1) pairs after
                for left in res[i]:
                    for right in res[k - i - 1]:
                        res[k].append("(" + left + ")" + right)

        return res[n]  # Return all valid combinations for n pairs