#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,a,b;
vector<vector<pair<int, int>>> adj_, adj;

void root(int x, int par) {
    for (auto &y : adj_[x]) {
        if (y.first == par) continue;

        adj[x].push_back(y);
        root(y.first, x);
    }
}

void dfs(int x, int lvl, int cur_idx) {
    if (!adj[x].size()) b = max(b, lvl);

    for (auto &[y,idx] : adj[x]) {
        if (cur_idx <= idx) dfs(y, lvl, idx);
        else dfs(y, lvl+1, idx);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj_.assign(n+1, vector<pair<int, int>>());
        adj.assign(n+1, vector<pair<int, int>>());

        for (int i = 0; i < n-1; i++) {
            cin >> a >> b;
            adj_[a].push_back({b,i});
            adj_[b].push_back({a,i});
        }

        root(1, -1);

        b = 0;
        dfs(1, 1, 0);
        cout << b << '\n';
    }
}