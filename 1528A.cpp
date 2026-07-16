#include <iostream>
#include <algorithm>
#include <vector>
#define ll long long
using namespace std;

int t,n,m,a,b;
vector<vector<int>> adj;
vector<vector<ll>> dp;
vector<int> l, r;

// state 0 = min, state 1 = max
ll recur(int node, int state, int parent) {
    if (dp[node][state] != -1) return dp[node][state];

    ll ans = 0, cur_val = state ? r[node] : l[node];

    for (auto x : adj[node]) {
        if (x == parent) continue;

        ans += max(recur(x, 0, node) + abs(cur_val-l[x]),
                   recur(x, 1, node) + abs(cur_val-r[x]));
    }

    return dp[node][state] = ans;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n+1, vector<int>());
        l.resize(n+1); r.resize(n+1);
        dp.assign(n+1, vector<ll>(2, -1));

        int node = -1;
        for (int i = 1; i <= n; i++) cin >> l[i] >> r[i];
        m = n; while (--m) {
            cin >> a >> b;
            if (node == -1) node = a;

            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        cout << max(recur(node, 0, -1), recur(node, 1, -1)) << '\n';
    }
    
}