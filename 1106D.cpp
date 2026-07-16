#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;
vector<int> path, vis;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.assign(n+1, vector<int>());

    while (m--) {
        cin >> a >> b;
        adj[a].emplace_back(b);
        adj[b].emplace_back(a);
    }

    for (auto& x : adj) sort(x.begin(), x.end());

    path.clear();
    vis.assign(n+1, 0);
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 1; i <= n; i++) {
        if (!vis[i]) {
            pq.push(i);

            while (!pq.empty()) {
                auto x = pq.top(); pq.pop();
                
                if (vis[x]) continue; vis[x] = 1;

                path.push_back(x);
                for (auto y : adj[x]) {
                    if (!vis[y]) pq.push(y);
                }
            }
        }
    }

    for (auto x : path) cout << x << ' ';
    cout << '\n';
}