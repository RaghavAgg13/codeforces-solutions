#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define ll long long

int t,n,m,a,b;
vector<vector<int>> adj;
vector<int> vis, inf, mult, ans;

void dfs(int root) {
    vis[root] = 1;
    ans[root] = 1;

    for (auto x : adj[root]) {
        if (!vis[x]) dfs(x);
        else if (vis[x] == 1) inf.push_back(x);
        else if (vis[x] == 2) mult.push_back(x);
    }

    vis[root] = 2;
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> t;
    while (t--) {
        queue<int> Q;
        
        cin >> n >> m;
        adj.assign(n+1, vector<int>());
        vis.assign(n+1, 0); inf.clear(); mult.clear(); ans.assign(n+1, 0);
        
        while (m--) {
            cin >> a >> b;
            adj[a].push_back(b);
        }
    
        dfs(1);
    
        for (auto x : inf) {
            if (ans[x] != -1) {
                ans[x] = -1;
                Q.push(x);
            }
        }
        while (!Q.empty()) {
            int cur = Q.front(); Q.pop();
    
            for (auto x : adj[cur]) {
                if (ans[x] != -1) {
                    ans[x] = -1;
                    Q.push(x);
                }
            }
        }
    
        for (auto x : mult) {
            if (ans[x] != -1 && ans[x] != 2) {
                ans[x] = 2;
                Q.push(x);
            }
        }
        while (!Q.empty()) {
            int cur = Q.front(); Q.pop();

            for (auto x : adj[cur]) {
                if (ans[x] != -1 && ans[x] != 2) {
                    ans[x] = 2;
                    Q.push(x);
                }
            }
        }
    
        for (int i = 1; i <= n; i++) cout << ans[i] << ' ';
        cout << '\n';
    }
}