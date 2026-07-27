#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<vector<int>> adj;
vector<bool> vis;

int dfs(int x) {
    if (vis[x]) return 0; vis[x] = 1;

    int sz = 1;
    for (auto y : adj[x]) {
        sz += dfs(y);
    }
    return sz;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> p(n);
        for (int i = 0; i < n; i++) {
            cin >> a; a--;
            p[i] = a; 
        }

        adj.assign(n, vector<int>());

        vector<int> arr(n, 0);
        for (int i = 0; i < n; i++) {
            if (p[i] == i || p[p[i]] == i) {
                arr[i] = 1;
                continue;
            }

            adj[i].push_back(p[i]);
        }

        int cnt = 0;

        vis.assign(n, false);
        for (int i = 0; i < n; i++) {
            if (!arr[i] && !vis[i]) {
                int sz = dfs(i);
                cnt += (sz-1)/2;
            }
        }
        cout << cnt << '\n';
    }
}