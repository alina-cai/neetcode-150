class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            cur = min(height[l], height[r]) * (r - l)
            res = max(res, cur)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            
        return res

# time: O(n)
# space: O(1)
