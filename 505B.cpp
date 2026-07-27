#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b,c;
vector<vector<vector<int>>> adj;

bool dfs(int x, int tar, int col, vector<bool>& vis) {
    if (x == tar) return true;
    vis[x] = true;
    
    for (int i = 1; i <= n; i++) {
        if (vis[i] || adj[x][i].empty()) continue;

        bool has_color = false;
        for (auto color : adj[x][i]) {
            if (color == col) {
                has_color = true;
                break;
            }
        }

        if (has_color && dfs(i, tar, col, vis)) return true;
    }
    return false;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.assign(n+1, vector<vector<int>>(n+1));

    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        adj[a][b].push_back(c);
        adj[b][a].push_back(c);
    }

    cin >> c;
    while (c--) {
        cin >> a >> b;
        int ans = 0;

        for (int col = 1; col <= m; col++) {
            vector<bool> vis(n+1, false);
            ans += dfs(a,b,col,vis);
        }

        cout << ans << '\n';
    }
}