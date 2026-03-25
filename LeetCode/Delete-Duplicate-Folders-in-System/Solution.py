1// links uses map
2struct Trie {
3    map<string, Trie*> links;
4    string id = "";
5    bool mark = 0;
6    Trie(string id = "") : id(id) {}
7
8    void insert(vector<string>& path) {
9        Trie* Node = this;
10        for (string& s : path) {
11            if (!Node->links.count(s))
12                Node->links[s] = new Trie(s);
13            Node = Node->links[s];
14        }
15    }
16};
17
18class Solution {
19public:
20    Trie trie;
21    unordered_map<string, Trie*> mp;
22    vector<vector<string>> ans;
23
24    string serial(Trie* Node) {
25        if (Node->links.empty())
26            return "";
27        string dir;
28        for (auto& [id, child] : Node->links)
29            dir += "(" + id + serial(child) + ")";
30
31        if (mp.count(dir)) {
32            mp[dir]->mark = 1;
33            Node->mark = 1;
34        } 
35        else
36            mp[dir] = Node;
37        //    cout<<dir<<endl;
38        return dir;
39    }
40
41    void to_ans(Trie* Node, vector<string>& path) {
42        for (auto& [id, child] : Node->links) {
43            if (child->mark)
44                continue;
45            path.push_back(id);
46            ans.push_back(path);
47            to_ans(child, path);
48            path.pop_back();
49        }
50    }
51
52    vector<vector<string>>
53    deleteDuplicateFolder(vector<vector<string>>& paths) {
54        for (auto& path : paths)
55            trie.insert(path);
56
57        serial(&trie);
58        vector<string> path;
59        to_ans(&trie, path);
60        return ans;
61    }
62};
63
64auto init = []() {
65    ios::sync_with_stdio(0);
66    cin.tie(0);
67    cout.tie(0);
68    return 'c';
69}();