class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        gmin = prices[0] 
        res = 0  # Fixed: Initialized 'res' before using it
        for r in range(len(prices)): 
            if prices[r] < gmin:  # Fixed: Compared price value instead of index 'r'
                gmin = prices[r] 
                l = r 
            res = max(res, prices[r] - gmin) 
        return res  # Fixed: Returned 'res' instead of the loop index 'r'
