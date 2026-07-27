#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj,b_;
vector<int> vis;

void dfs(int x, int par, int start, vector<int> &arr) {
    if (arr.size() == 3) {
        if (x == start) b_.push_back(arr);
        return;
    }

    for (auto y : adj[x]) {
        if (y == par) continue;

        arr.push_back(y);
        dfs(y, x, start, arr);
        arr.pop_back();
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.assign(n+1, vector<int>());
    b_.clear();
    vis.assign(n+1, 0);

    while (m--) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    } 

    for (int i = 1; i <= n; i++) {
        vector<int> arr;
        
        dfs(i, -1, i, arr);
    }

    int ans = 1e9;
    for (auto tp : b_) {
        b = 0;
        for (auto y : tp) b += adj[y].size()-2;
        ans = min(ans, b);
    }

    if (ans == 1e9) ans = -1;
    cout << ans;
}