#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;
#define ll long long

int n,m,s,a,b,c;

vector<vector<pair<int, int>>> adj,radj;
vector<int> vis, degree;

void dfs(int node, stack<int>& S) {
    vis[node] = 1;

    for (const auto& [x,wt] : adj[node]) {
        if (!vis[x]) dfs(x, S);
    }
    S.push(node);
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.assign(n+1, vector<pair<int, int>>()); radj.assign(n+1, vector<pair<int, int>>());
    vis.assign(n+1, 0); degree.assign(n+1, 0);

    while (m--) {
        cin >> a >> b >> c;
        adj[a].emplace_back(b, c);
        radj[b].emplace_back(a, c);
    }

    // kosaraju
    stack<int> S;
    for (int i = 1; i <= n; i++) {
        if (!vis[i]) dfs(i, S);
    }

    fill(vis.begin(), vis.end(), 0);
    int idx = 0;
    vector<int> scc(n+1, 0);
    queue<int> Q;

    while (!S.empty()) {
        auto x = S.top(); S.pop();
        if (vis[x]) continue; vis[x] = 1;
        
        scc[x] = idx;
        
        Q.push(x);
        while (!Q.empty()) {
            auto cur = Q.front(); Q.pop();
            
            for (const auto& [c,wt] : radj[cur]) {
                if (vis[c]) continue; vis[c] = 1; 
                
                scc[c] = idx;
                Q.push(c);
            }
        }
        idx++;
    }
    
    vector<ll> weight(n+1, 0);
    vector<vector<pair<int, ll>>> new_adj(idx+1);
    for (int i = 1; i <= n; i++) {
        for (const auto& [y,wt] : adj[i]) {
            if (scc[i] == scc[y]) {
                ll k = (-1 + sqrt(1.0+8.0*wt))/2;
                weight[scc[i]] += (k+1)*wt - (k*(k+1)*(k+2))/6;
            }
            else new_adj[scc[i]].emplace_back(scc[y], wt);
        }
    }

    cin >> s;
    queue<pair<int, ll>> q;
    vector<ll> dist(idx+1, 0);
    dist[scc[s]] = weight[scc[s]];
    q.push({scc[s], dist[scc[s]]});

    while (!q.empty()) {
        auto [x,wt] = q.front(); q.pop();
        if (wt < dist[x]) continue;

        for (const auto& [cur, w] : new_adj[x]) {
            if (wt+w+weight[cur] <= dist[cur]) continue;
            dist[cur] = wt+w+weight[cur];
            q.push({cur, dist[cur]});
        }
    }

    ll ans = 0;
    for (int i = 0; i < idx; i++) ans = max(ans, dist[i]);
    cout << ans << '\n';
}