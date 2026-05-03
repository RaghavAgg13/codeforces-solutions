#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <functional>
using namespace std;
#define ll long long

int n,m,s,a,b,c;

vector<vector<pair<int, int>>> adj,radj;
vector<int> vis, degree;

void dfs(int node, stack<int>& S) {
    vis[node] = 1;

    for (auto& [x,wt] : adj[node]) {
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
            
            for (auto& [c,wt] : radj[cur]) {
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
        for (auto& [y,wt] : adj[i]) {
            if (scc[i] == scc[y]) {
                ll k = (-1 + sqrt(1 + 8ll*wt))/2;
                weight[scc[i]] += (k+1)*wt - (k*(k+1)*(k+2))/6;
            }
            else new_adj[scc[i]].emplace_back(scc[y], wt);
        }
    }

    cin >> s;
    vector<ll> dist(idx+1, -1);

    function<ll(int)> solve = [&](int u) {
        if (dist[u] != -1) return dist[u];

        ll ans = 0;
        for (auto& [v,w] : new_adj[u]) {
            ans = max(ans, w+solve(v));
        }
        return dist[u] = weight[u]+ans;
    };

    cout << solve(scc[s]);
}