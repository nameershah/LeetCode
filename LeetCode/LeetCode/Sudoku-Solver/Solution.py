1class Solution:
2    def solveSudoku(self, board: list[list[str]]) -> None:
3        # bitmasks for rows, columns, and 3x3 boxes
4        rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
5        
6        def get_box(r, c): return (r // 3) * 3 + (c // 3)
7
8        # Initialise masks and track empty cells
9        empty_cells = []
10        for r in range(9):
11            for c in range(9):
12                if board[r][c] != '.':
13                    val = int(board[r][c]) - 1
14                    mask = 1 << val
15                    rows[r] |= mask
16                    cols[c] |= mask
17                    boxes[get_box(r, c)] |= mask
18                else:
19                    empty_cells.append((r, c))
20
21        def solve():
22            if not empty_cells:
23                return True
24            
25            # MRV Heuristic: Find cell with the fewest remaining candidates
26            # This is the "secret sauce" for 20ms performance
27            min_options = 10
28            best_idx = -1
29            best_taken_mask = 0
30            
31            for i in range(len(empty_cells)):
32                r, c = empty_cells[i]
33                taken = rows[r] | cols[c] | boxes[get_box(r, c)]
34                # Count available numbers (0 bits in the 9-bit mask)
35                count = bin(~taken & 0x1FF).count('1')
36                
37                if count == 0: return False  # Prune early: no valid moves
38                if count < min_options:
39                    min_options = count
40                    best_idx = i
41                    best_taken_mask = taken
42                    if count == 1: break  # Optimization: can't beat 1 option
43
44            r, c = empty_cells.pop(best_idx)
45            
46            # Try only the bits that are NOT in the 'taken' mask
47            for num in range(9):
48                if not (best_taken_mask & (1 << num)):
49                    mask = 1 << num
50                    board[r][c] = str(num + 1)
51                    rows[r] |= mask
52                    cols[c] |= mask
53                    boxes[get_box(r, c)] |= mask
54                    
55                    if solve(): return True
56                    
57                    # Backtrack (Bitwise XOR is faster than removal from sets)
58                    rows[r] ^= mask
59                    cols[c] ^= mask
60                    boxes[get_box(r, c)] ^= mask
61            
62            # Restore state for backtracking
63            empty_cells.insert(best_idx, (r, c))
64            board[r][c] = "."
65            return False
66
67        solve()