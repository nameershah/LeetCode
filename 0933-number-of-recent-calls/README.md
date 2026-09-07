## 969. Number of Recent Calls

**Difficulty:** Easy

[LeetCode Problem](https://leetcode.com/problems/number-of-recent-calls/)

### Problem

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

- `RecentCounter()` initializes the counter with zero recent requests.
- `int ping(int t)` adds a new request at time `t`, where `t` represents time in milliseconds, and returns the number of requests that have happened in the past `3000` milliseconds.
- Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

### Example 1

**Input:**

```text
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
```

**Output:**

```text
[null, 1, 2, 3, 3]
```

**Explanation:**

```text
RecentCounter recentCounter = new RecentCounter();

recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1,100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1,100,3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1,100,3001,3002], range is [2,3002], return 3
```

### Constraints

- `1 <= t <= 10^9`
- Each test case calls `ping` with **strictly increasing** values of `t`.
- At most `10^4` calls will be made to `ping`.

### Approach

Use a **queue** to store the timestamps of recent requests.

For every call to `ping(t)`:

1. Add the new timestamp `t` to the queue.
2. Remove timestamps that are smaller than `t - 3000`.
3. Return the current size of the queue.

Because `t` is strictly increasing, each timestamp is added and removed at most once.

### Complexity

- **Time:** `O(n)` overall
- **Space:** `O(n)`

### 🔗 To Recall

For the original solution, implementation, and notes, refer to the Google Colab notebook:

**[Open Google Colab — Number of Recent Calls](https://colab.research.google.com/drive/1VK_D8hcdC4y1CZ3MgQyt72dKydiG-BDe?usp=sharing#scrollTo=CgjOl_oTzsSK)**
