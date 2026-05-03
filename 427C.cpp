#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;
#define ll long long

int n,m,s,a,b;

vector<vector<int>> adj,radj;
vector<int> vis, degree, cost;

void dfs(int node, stack<int>& S) {
    vis[node] = 1;

    for (auto x : adj[node]) {
        if (!vis[x]) dfs(x, S);
    }
    S.push(node);
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>()); radj.assign(n+1, vector<int>());
    vis.assign(n+1, 0); degree.assign(n+1, 0); cost.assign(n+1, 0);

    for (int i = 1; i <= n; i++) cin >> cost[i];
    
    cin >> m;
    while (m--) {
        cin >> a >> b;
        adj[a].push_back(b);
        radj[b].push_back(a);
    }

    // kosaraju
    stack<int> S;
    for (int i = 1; i <= n; i++) {
        if (!vis[i]) dfs(i, S);
    }

    vis.assign(n+1, 0);

    queue<int> Q;
    int idx = 0;
    vector<int> scc(n+1, 0);
    while (!S.empty()) {
        auto x = S.top(); S.pop();
        if (vis[x]) continue; vis[x] = 1;
        
        scc[x] = idx;

        Q.push(x);
        while (!Q.empty()) {
            auto cur = Q.front(); Q.pop();

            for (auto c : radj[cur]) {
                if (vis[c]) continue; vis[c] = 1; 

                scc[c] = idx;
                Q.push(c);
            }
        }
        idx++;
    }

    vector<int> min_cost(idx+1, 1e9), cnt(idx+1, 0);
    for (int i = 1; i <= n; i++) {
        if (cost[i] < min_cost[scc[i]]) {
            min_cost[scc[i]] = cost[i];
            cnt[scc[i]] = 1;
        }
        else if (cost[i] == min_cost[scc[i]]) cnt[scc[i]]++;
    }

    ll total_cost = 0, ways = 1;
    for (int i = 0; i < idx; i++) {
        total_cost += min_cost[i];
        ways = (ways*cnt[i])%1000000007;
    }

    cout << total_cost << ' ' << ways << '\n';
}