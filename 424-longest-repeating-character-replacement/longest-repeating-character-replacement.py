class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        fMax = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            fMax = max(fMax, count[s[r]])

            while (r - l + 1) - fMax > k:
                count[s[l]] -= 1
                l += 1

        return r - l + 1

# time: O(n)
# space: O(1)
