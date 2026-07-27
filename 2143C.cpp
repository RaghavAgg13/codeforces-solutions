#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int t,n,m,a,b,x,y;
vector<vector<int>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n+1, vector<int>());
        vector<int> in(n+1, 0);

        m = n; while (--m) {
            cin >> a >> b >> x >> y;
            if (a > b) swap(a,b);

            if (x >= y) {
                adj[b].push_back(a);
                in[a]++;
            }
            else {
                adj[a].push_back(b);
                in[b]++;
            }
        }
        
        queue<int> q;
        vector<int> p(n+1);
        int val = 1;
        for (int i = 1; i <= n; i++) {
            if (!in[i]) q.push(i);
        }

        while (!q.empty()) {
            auto x = q.front(); q.pop();
            p[x] = val++;

            for (auto y : adj[x]) {
                if (--in[y] == 0) q.push(y);
            }
        }

        for (int i = 1; i <= n; i++) cout << p[i] << ' ';
        cout << '\n';
    }
}