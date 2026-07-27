#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<vector<pair<int, int>>> adj;
vector<int> ans; 

int dfs(int x, int par) {
    if (adj[x].size() >= 3) return 1;
    if (adj[x].size() == 1) b = x;

    int val = 0;
    for (auto y : adj[x]) {
        if (y.first == par) continue;
        val = max(val, dfs(y.first, x));
    }
    return val;
}

void set(int x, int par, int prime) {
    for (auto y : adj[x]) {
        if (y.first == par) continue;

        ans[y.second] = prime;
        
        set(y.first, x, (prime==2) ? 3 : 2);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n+1, vector<pair<int, int>>());
        ans.resize(n-1);
        
        for (int i = 0; i < n-1; i++) {
            cin >> a >> b;
            adj[a].push_back({b,i});
            adj[b].push_back({a,i});
        }

        int val = dfs(1, -1);
        if (val) {
            cout << "-1\n";
            continue;
        }

        set(b, -1, 2);

        for (auto x : ans) cout << x << ' ';
        cout << '\n';
    }
}