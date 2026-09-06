1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = float("inf")
4        max_profit = 0
5
6        for price in prices:
7            if price < min_price:
8                min_price = price
9            elif price - min_price > max_profit:
10                max_profit = price - min_price
11        return max_profit