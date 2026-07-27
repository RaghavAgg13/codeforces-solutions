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
        color.assign(n+1, -1);
        adj.assign(n+1, vector<int>());

        while (m--) {
            cin >> a >> b;
            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        vector<int> c1,c2;
        
        queue<int> q; q.push(1);
        color[1] = 1;
        c1.push_back(1);

        while (!q.empty()) {
            auto x = q.front(); q.pop();

            for (auto y : adj[x]) {
                if (color[y] != -1) continue; color[y] = 1-color[x];

                if (color[y] == 1) c1.push_back(y);
                else c2.push_back(y);

                q.push(y);
            }
        }

        if (c1.size() < c2.size()) c2 = c1;

        cout << c2.size() << '\n';
        for (auto &x : c2) cout << x << ' ';
        cout << '\n';
    }
}