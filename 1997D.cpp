#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<vector<int>> adj;
vector<int> val;

void solve(int x) {
    if (adj[x].size() == 0) return;

    int sz = 1e9;
    for (auto y : adj[x]) {
        solve(y);
        sz = min(sz, val[y]);
    }

    if (x == 1) val[x] += sz;
    else if (sz > val[x]) val[x] = (val[x]+sz)/2;
    else val[x] = sz;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        val.resize(n+1);
        adj.assign(n+1, vector<int>());

        for (int i = 1; i <= n; i++) cin >> val[i];

        for (int i = 2; i <= n; i++) {
            cin >> a;
            adj[a].push_back(i);
        }

        solve(1);
        cout << val[1] << '\n';
    }
}