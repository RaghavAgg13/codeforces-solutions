#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b,c,sz;
vector<vector<int>> adj;
vector<pair<int, int>> edges;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.resize(n+1, vector<int>());
    edges = {{-1,-1}};
    sz = 0;

    while (n--) {
        cin >> a >> b >> c;

        if (a == 1) {
            b += 1e9; c += 1e9;

            sz++;
            edges.push_back({b,c});

            for (int i = 0; i < sz; i++) {
                auto [x,y] = edges[i];

                if ((b < x && x < c) || (b < y && y < c)) {
                    adj[i].push_back(sz);
                }
                if ((x < b && b < y) || (x < c && c < y)) {
                    adj[sz].push_back(i);
                }
            }
        }
        else {
            vector<int> vis(sz+1, 0);

            queue<int> q; q.push(b);
            vis[b] = 1;

            bool found = false;
            while (!q.empty()) {
                auto x = q.front(); q.pop();

                for (auto y : adj[x]) {
                    if (vis[y]) continue; vis[y] = 1;
                    
                    if (y == c) {
                        found = true;
                        break;
                    }

                    q.push(y);
                }
            }

            if (found) cout << "YES\n";
            else cout << "NO\n";
        }

    }
    
}