#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b,c;
vector<vector<pair<int, int>>> adj;
vector<vector<int>> tree;
vector<int> q;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    q.resize(n+1);
    adj.assign(n+1, vector<pair<int, int>>());
    tree.assign(n+1, vector<int>());

    for (int i = 1; i <= n; i++) cin >> q[i];

    cin >> m;
    while (m--) {
        cin >> a >> b >> c;

        adj[b].push_back({a,c});
    }

    int cost = 0, no_sup = 0;

    for (int i = 1; i <= n; i++) {
        int co = 1e9, y_ = -1;

        for (auto [y,c] : adj[i]) {
            if (c < co && q[i] < q[y]) {
                co = c;
                y_ = y;
            }
        }

        if (y_ == -1) {
            no_sup++;
            continue;
        }

        tree[y_].push_back(i);
        cost += co;
    }

    if (no_sup != 1) cout << -1;
    else cout << cost;
}