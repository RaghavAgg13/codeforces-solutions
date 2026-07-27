#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,a;
vector<vector<int>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.resize(n+1, vector<int>());

    for (int i = 2; i <= n; i++) {
        cin >> a;
        adj[a].push_back(i);
        adj[i].push_back(a);
    }

    vector<int> from(n+1, -1);

    queue<pair<int, int>> q;
    q.push({n, -1});
    while (!q.empty()) {
        auto [x,par] = q.front(); q.pop();

        if (x == 1) {
            while (from[x] != -1) {
                cout << x << ' ';
                x = from[x];
            }
            cout << n;
            return 0;
        }

        for (auto y : adj[x]) {
            if (y == par) continue;

            from[y] = x;
            q.push({y, x});
        }
    }
}