#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long

int t,n,m,k,a,b;
vector<vector<int>> adj;
vector<ll> cost;
vector<int> unl,vis;

ll min_cst(int x) {
    if (vis[x]) return cost[x];
    vis[x] = 1;

    if (unl[x]) return cost[x] = 0;
    if (adj[x].empty()) return cost[x];

    ll cst = 0;
    for (auto y : adj[x]) {
        cst += min_cst(y);
    }
    return cost[x] = min(cost[x], cst);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> k;
        cost.resize(n+1);
        unl.assign(n+1, 0);
        vis.assign(n+1, 0);
        adj.assign(n+1, vector<int>());

        for (int i = 1; i <= n; i++) cin >> cost[i];
        while (k--) {
            cin >> a;
            unl[a] = 1;
        }

        for (int i = 1; i <= n; i++) {
            cin >> a;
            for (int j = 0; j < a; j++) {
                cin >> b;
                adj[i].push_back(b);
            }
        }

        for (int i = 1; i <= n; i++) min_cst(i);

        for (int i = 1; i <= n; i++) cout << cost[i] << ' ';
        cout << '\n';
    }
}