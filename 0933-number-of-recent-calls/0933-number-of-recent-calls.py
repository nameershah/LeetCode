from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        # 1. Add the new request
        self.q.append(t)

        # 2. Remove requests that are too old
        while self.q[0] < t - 3000:
            self.q.popleft()

        # 3. Return the number of recent requests
        return len(self.q)