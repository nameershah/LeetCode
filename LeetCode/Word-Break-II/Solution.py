1class Solution:
2    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
3        # Step 1: Convert wordDict to a set for O(1) lookups
4        word_set = set(wordDict)
5        # Memoization dictionary to store results for subproblems
6        memo = {}
7
8        def dfs(start_idx):
9            # If we've calculated results for this substring starting position, return it
10            if start_idx in memo:
11                return memo[start_idx]
12            
13            # Base case: If we reached the end, return an empty string/list
14            if start_idx == len(s):
15                return [""]
16
17            results = []
18            # Try every possible split point from start_idx + 1 to len(s)
19            for end_idx in range(start_idx + 1, len(s) + 1):
20                word = s[start_idx:end_idx]
21                
22                # If current substring is a valid word
23                if word in word_set:
24                    # Recursively get sentences for the remaining substring
25                    sub_sentences = dfs(end_idx)
26                    
27                    # For each sub-sentence, build the current sentence
28                    for sub in sub_sentences:
29                        if sub == "":
30                            results.append(word)
31                        else:
32                            results.append(word + " " + sub)
33            
34            # Store result in memo
35            memo[start_idx] = results
36            return results
37
38        # Start recursion from index 0
39        return dfs(0)