class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        l = 0
        r = len(height) - 1
        lMax = height[l]
        rMax = height[r]

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]

        return res

# time: O(n)
# space: O(1)
