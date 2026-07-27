#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#define ll long long
using namespace std;

int n,m,k,a,b,c;
vector<vector<pair<int, int>>> adj;
vector<ll> dist;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;
    adj.assign(n+1, vector<pair<int, int>>());
    dist.assign((n+1)*(k+1), 1e18);

    while (m--) {
        cin >> a >> b >> c;

        adj[a].emplace_back(b,c);
        adj[b].emplace_back(a,c);
    }
    
    // dist, node*(k+1) + flight
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;
    pq.push({0, 1*(k+1)+0});
    dist[k+1] = 0;

    while (!pq.empty()) {
        auto [d, state] = pq.top(); pq.pop();
        int node = state/(k+1), flight = state%(k+1);

        if (d > dist[state]) continue;

        for (auto [x, d_] : adj[node]) {
            int next_state = x*(k+1)+flight;
            if (d+d_ >= dist[next_state]) continue;
            dist[next_state] = d+d_;

            pq.push({d+d_, next_state});
        }

        if (flight < k) {
            for (int x = 1; x <= n; x++) {
                ll f = 1LL*(node-x)*(node-x);
                int next_state = x*(k+1)+flight+1;
                if (d+f >= dist[next_state]) continue;

                dist[next_state] = d+f;
                pq.push({d+f, next_state});
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        ll ans = 1e18;
        for (int j = 0; j <= k; j++)
            ans = min(ans, dist[i*(k+1)+j]);
        cout << ans << ' ';
    }
    
    cout << '\n';
}