class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = float('inf')

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return res

# time: O(log(n))
# space: O(1)
