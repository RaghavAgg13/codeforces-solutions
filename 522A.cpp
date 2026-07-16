#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int n,no,a,b,root;
string s1,s2;
vector<vector<int>> adj;
unordered_map<string, int> map;

void dfs(int root, int depth, int parent) {
    b = max(b, depth);

    for (auto x : adj[root]) {
        if (x == parent) continue;

        dfs(x, depth+1, root);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+2, vector<int>());
    
    no = 1;
    map.clear();
    map["polycarp"] = 0;

    while (n--) {
        cin >> s1 >> s2 >> s2;
        for (char &c : s1) c = tolower(c);
        for (char &c : s2) c = tolower(c);
        
        if (map.find(s1) == map.end()) map[s1] = no++;
        if (map.find(s2) == map.end()) map[s2] = no++;
        a = map[s1]; b = map[s2];

        adj[b].push_back(a);
    }
    
    b = 0;
    dfs(0, 1, -1);
    
    cout << b << '\n';
}