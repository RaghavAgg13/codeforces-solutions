#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int t,n,k,m,a,b;
vector<vector<int>> adj;
vector<int> lvl, degree;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> k;
        adj.assign(n+1, vector<int>());
        lvl.assign(n+1, k+1);
        degree.assign(n+1, 0);

        m = n; while (--m) {
            cin >> a >> b;
            adj[a].push_back(b);
            adj[b].push_back(a);
            degree[a]++; degree[b]++;
        }    

        queue<int> q;
        for (int i = 1; i <= n; i++) {
            if (degree[i] <= 1) {
                lvl[i] = 1;
                q.push(i);
            }
        }

        while (!q.empty()) {
            auto x = q.front(); q.pop();

            for (auto y : adj[x]) {
                if (lvl[y] != k+1) continue;

                if (--degree[y] <= 1) {
                    lvl[y] = lvl[x]+1;
                    if (lvl[y] < k) q.push(y);
                }
            }
        }

        b = 0;
        for (int i = 1; i <= n; i++) {
            if (lvl[i] > k) b++;
        }
        cout << b << '\n';
    }
}