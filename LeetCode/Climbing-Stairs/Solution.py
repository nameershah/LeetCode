1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 2:
4            return n 
5        a, b = 1, 2  
6        for _ in range(3, n+1):
7            a,b = b, a + b
8        return b
9        