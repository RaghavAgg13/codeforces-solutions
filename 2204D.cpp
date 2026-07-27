#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int t,n,m,a,b;
vector<vector<int>> adj;
vector<int> color;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> m;
        adj.assign(n+1, vector<int>());

        while (m--) {
            cin >> a >> b;
            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        color.assign(n+1, -1);

        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (color[i] != -1) continue; color[i] = 1;

            queue<int> q;
            q.push(i);
            bool valid = true;
            int color1 = 1, color0 = 0;

            while (!q.empty()) {
                auto x = q.front(); q.pop();

                for (auto y : adj[x]) {
                    if (color[y] == color[x]) valid = false;
                    if (color[y] != -1) continue;

                    color[y] = 1-color[x];
                    if (color[y]) color1++;
                    else color0++;

                    q.push(y);
                }
            }

            if (valid) ans += max(color0, color1);
        }
        cout << ans << '\n';
    }
}