class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]

        for p in prices:
            if p < lowest:
                lowest = p

            res = max(res, p - lowest)

        return res

# time: O(n)
# space: O(1)
