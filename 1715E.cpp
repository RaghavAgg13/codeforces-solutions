#include <iostream>
#include <algorithm>
#include <vector>
#include <array>
#include <queue>
#define ll long long
using namespace std;

int n,m,k,a,b,c;
vector<vector<pair<int, ll>>> adj;
vector<vector<ll>> dist;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;
    adj.assign(n+1, vector<pair<int, ll>>());
    dist.assign(n+1, vector<ll>(k+1, 1e18));

    while (m--) {``
        cin >> a >> b >> c;

        adj[a].emplace_back(b,c);
        adj[b].emplace_back(a,c);
    }
    
    // dist, node, flights
    priority_queue<array<ll, 3>, vector<array<ll, 3>>, greater<array<ll, 3>>> pq;
    pq.push({0, 1, 0});
    dist[1][0] = 0;

    while (!pq.empty()) {
        auto arr = pq.top(); pq.pop();
        auto d = arr[0], node = arr[1], flight = arr[2];

        if (d > dist[node][flight]) continue;

        for (auto [x,d_] : adj[node]) {
            if (d+d_ >= dist[x][flight]) continue;
            dist[x][flight] = d+d_;

            pq.push({d+d_, x, flight});
        }

        if (flight < k) {
            for (int x = 1; x <= n; x++) {
                ll f = 1LL*(node-x)*(node-x);
                if (d+f >= dist[x][flight+1]) continue;

                dist[x][flight+1] = d+f;
                pq.push({d+f, x, flight+1});
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        ll ans = 1e18;
        for (int j = 0; j <= k; j++)
            ans = min(ans, dist[i][j]);
        cout << ans << ' ';
    }
    
    cout << '\n';
}