# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not (1 <= len(prices) <= 10**5):
            raise ValueError("Lenght of prices list must be in [1, 10**5]")

        max_profit = 0
        buy = 10**4 + 1

        for price in prices:
            if not (0 <= price <= 10**4):
                raise ValueError("Values of prices list must be in [0, 10**4]")

            if price < buy:
                buy = price
            elif price > buy:
                max_profit = max(max_profit, price - buy)

        return max_profit
