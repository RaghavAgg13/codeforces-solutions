#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <climits>
using namespace std;
#define ll long long

int n,m,a,b,c;

struct cmp {
    bool operator()(const pair<int, ll>& a, const pair<int, ll>& b) const {
        return a.second > b.second;
    }
};

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    vector<vector<pair<int, int>>> adj(n+1);
    vector<int> from(n+1, -1);
    vector<ll> dist(n+1, LLONG_MAX);

    while (m--) {
        cin >> a >> b >> c;
        adj[a].emplace_back(b,c);
        adj[b].emplace_back(a,c);
    }

    for (int i = 1; i <= n; ++i) {
        adj[i].shrink_to_fit();
    }

    priority_queue<pair<int, ll>, vector<pair<int, ll>>, cmp> pq;
    pq.push({1, 0});

    dist[1] = 0;
    while (!pq.empty()) {
        auto [cur, d] = pq.top(); pq.pop();
        
        if (d > dist[cur]) continue;
        if (cur == n) break;
        
        for (auto [x, d_] : adj[cur]) {
            if (d+d_ >= dist[x]) continue;
            dist[x] = d+d_; from[x] = cur;
            
            pq.push({x, dist[x]});
        }
    }

    vector<int> pos;
    while (from[n] != -1) {
        pos.push_back(n);
        n = from[n];
    }

    if (dist[n] == LLONG_MAX) {
        cout << "-1\n";
        return 0;
    }

    pos.push_back(1);
    reverse(pos.begin(), pos.end());

    for (auto x : pos) cout << x << ' ';
    cout << '\n';
}