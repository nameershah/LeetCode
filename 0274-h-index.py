class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # 1. Sort descending: O(n log n)
        citations.sort(reverse=True)
        
        h = 0
        
        # 2. Iterate through papers: O(n)
        for i, c in enumerate(citations):
            rank = i + 1
            
            if c >= rank:
                h = rank  # Save the highest passing rank so far
            else:
                break     # Stop early once citations drop below rank
                
        return h
