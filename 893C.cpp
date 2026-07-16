#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;
vector<int> gold, vis;

void dfs(int x) {
    vis[x] = 1;

    for (auto y : adj[x]) {
        if (!vis[y]) dfs(y);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.assign(n+1, vector<int>());
    gold.resize(n+1);

    for (int i = 1; i <= n; i++) cin >> gold[i];
    while (m--) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    for (int i = 1; i <= n; i++) pq.push({gold[i], i});
    vis.assign(n+1, 0);

    long long cost = 0;
    while (!pq.empty()) {
        auto [c, x] = pq.top(); pq.pop();

        if (vis[x]) continue;
        cost += c;
        dfs(x);
    }

    cout << cost << '\n';
}