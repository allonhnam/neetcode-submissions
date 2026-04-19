class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Append the length of the string, a separator '#', and the string itself
            # This ensures we know where each string starts and ends during decoding
            res += str(len(s)) + "#" + s
        return res  # Returns a single encoded string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Find the position of '#' to get the length prefix
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Extract length of the next string
            i = j + 1             # Move past the '#' character
            j = i + length        # j now points to the end of the current string
            res.append(s[i:j])    # Extract and append the string to result
            i = j                 # Move to the start of the next encoded string
        return res  # Returns the list of original strings
