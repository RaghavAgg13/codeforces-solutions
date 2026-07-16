#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;
vector<int> parent;

int find(int u) {
    while (parent[u] >= 0) {
        if (parent[parent[u]] >= 0) parent[u] = parent[parent[u]];
        u = parent[u];
    }

    return u;
}

void merge(int u, int v) {
    u = find(u); v = find(v);

    if (u == v) return;

    if (parent[u] <= parent[v]) {
        parent[u] += parent[v];
        parent[v] = u;
    } else {
        parent[v] += parent[u];
        parent[u] = v;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.resize(n+1, vector<int>());
    parent.assign(n+1, -1);

    while (m--) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);

        merge(a,b);
    }

    vector<int> vis(n+1, 0);
    vector<vector<int>> grps(n+1, vector<int>());
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        if (!vis[find(i)]) {
            vis[find(i)] = 1;
        }
        grps[find(i)].push_back(i);
    }

    bool found = true;
    for (int i = 1; i <= n; i++) {
        if (!grps[i].size()) continue;

        long long cnt = 0, k = grps[i].size();
        for (auto x : grps[i]) cnt += adj[x].size();
        if (cnt != k*k-k) {
            found = false;
            break;
        }
    }

    if (found) cout << "YES\n";
    else cout << "NO\n";
}