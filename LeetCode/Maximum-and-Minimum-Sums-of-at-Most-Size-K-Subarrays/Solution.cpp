1#include <bits/stdc++.h>
2
3using namespace std;
4
5#define ll                              long long
6#define mod97                           (int)(1e9+7)
7#define mod53                           998244353
8#define phi                             acos(-1)
9#define infy_ll                         (ll)1e18+10
10#define infy_int                        (int)1e9+10
11#define all(x)                          x.begin(), x.end()
12
13typedef vector<int>                     vint;
14typedef vector<vint>                    vvint;
15typedef pair<int,int>                   pii;
16typedef pair<ll,ll>                     pll;
17typedef vector<pii>                     vpii;
18typedef vector<pll>                     vpll;
19typedef vector<vpii>                    vvpii;
20typedef vector<bool>                    vbool;
21typedef vector<string>                  vstr;
22typedef vector<ll>                      vll;
23typedef vector<vll>                     vvll;
24
25class Solution {
26public:
27    ll minMaxSubarraySum(vector<int>& nums, int k) {
28        int n = nums.size();
29        vpll qmin, qmax;
30        ll res = 0;
31        for(int i = 0; i < n; i++) {
32            while(!qmin.empty() && nums[i] <= nums[qmin.back().first]) qmin.pop_back();
33            if(qmin.empty()) {
34                qmin.push_back({i, (ll)(i+1)*nums[i]});
35            } else {
36                auto [j, sj] = qmin.back();
37                qmin.push_back({i, (ll)(i - j)*nums[i]+sj});
38            }
39
40            while(!qmax.empty() && nums[i] >= nums[qmax.back().first]) qmax.pop_back();
41            if(qmax.empty()) {
42                qmax.push_back({i, (ll)(i+1)*nums[i]});
43            } else {
44                auto [j, sj] = qmax.back();
45                qmax.push_back({i, (ll)(i - j)*nums[i]+sj});
46            }
47            int l = max(-1, i-k);
48            auto v = make_pair(l, infy_ll);
49
50            int j = upper_bound(all(qmin), v) - qmin.begin();
51            res += qmin.back().second - qmin[j].second;
52            res += (ll)(qmin[j].first - l) * nums[qmin[j].first];
53
54            j = upper_bound(all(qmax), v) - qmax.begin();
55            res += qmax.back().second - qmax[j].second;
56            res += (ll)(qmax[j].first - l) * nums[qmax[j].first];
57        }
58
59        return res;
60    }
61};