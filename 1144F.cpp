#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<pair<int, int>>> adj;
vector<int> dir,vis;

void dfs(int x, int par, int d) {
    vis[x] = 1;

    for (auto [y,i] : adj[x]) {
        if (y == par) continue;   

        int edge_idx = abs(i);
        int expected_dir = (i>0) ? d : 1-d;

        if (dir[edge_idx] == 1-expected_dir) {
            b = -1;
            return;
        }
        dir[edge_idx] = expected_dir;

        if (y == par || vis[y]) continue;
        dfs(y, x, 1-d);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.assign(n+1, vector<pair<int, int>>());
    dir.assign(m+1, -1);
    vis.assign(m+1, 0);

    for (int i = 1; i <= m; i++) {
        cin >> a >> b;
        adj[a].push_back({b,i});
        adj[b].push_back({a,-i});
    }

    b = 0;
    dfs(1, -1, 1);

    if (b == -1) cout << "NO";
    else {
        cout << "YES\n";
        for (int i = 1; i <= m; i++) cout << dir[i];
    }
}