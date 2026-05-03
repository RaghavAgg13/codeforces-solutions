#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <array>
using namespace std;
#define ll long long

int n,m,k,a,b,c;

struct cmp {
    bool operator()(const array<ll, 3>& a, const array<ll, 3>& b) const {
        return a[1] > b[1];
    }
};

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;
    vector<vector<pair<int, ll>>> adj(n+1);
    vector<vector<ll>> dist(n+1, vector<ll>(k+1, 1e18));

    while (m--) {
        cin >> a >> b >> c;
        adj[a].emplace_back(b,c);
        adj[b].emplace_back(a,c);
    }

    priority_queue<array<ll, 3>, vector<array<ll, 3>>, cmp> pq;
    pq.push({1, 0, 0});

    dist[1][0] = 0;
    while (!pq.empty()) {
        auto arr = pq.top(); pq.pop();
        ll cur = arr[0], d = arr[1], flights = arr[2];
        
        if (d > dist[cur][flights] || flights > k) continue;
        
        for (auto [x, d_] : adj[cur]) {
            if (d+d_ < dist[x][flights]) {
                dist[x][flights] = d+d_;
                pq.push({x, dist[x][flights], flights});
            }
        }
        
        if (flights < k) {
            for (int x = 1; x <= n; x++) {
                ll f = (cur-x)*(cur-x);
                if (d+f < dist[x][flights+1]) {
                    dist[x][flights+1] = d+f;
                    pq.push({x, dist[x][flights+1], flights+1});
                }
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        ll ans = 1e18;
        for (int j = 0; j <= k; j++) ans = min(ans, dist[i][j]);
        cout << ans << ' ';
    }
}