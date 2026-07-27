#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b,c;
vector<int> in, out;
vector<vector<pair<int, int>>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    in.assign(n+1, 0); out.assign(n+1, 0);
    adj.assign(n+1, vector<pair<int, int>>());

    while (m--) {
        cin >> a >> b >> c;
        in[b]++; out[a]++;

        adj[a].push_back({b,c});
    }

    queue<int> q;
    vector<vector<int>> ans;
    for (int i = 1; i <= n; i++) {
        if (out[i] && !in[i]) q.push(i);
        else continue;

        int diam = (int)1e9;
        while (!q.empty()) {
            auto x = q.front(); q.pop();
            if (!out[x]) ans.push_back({i, x, diam});

            int val = 0;
            for (auto [y,d] : adj[x]) {
                diam = min(diam, d);
                q.push(y);
            }
        }
    }

    cout << ans.size() << '\n';
    for (auto arr : ans) {
        for (auto x : arr) cout << x << ' ';
        cout << '\n';
    }
}