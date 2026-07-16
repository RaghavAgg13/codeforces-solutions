#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());

    m = n; while (--m) {
        cin >> a >> b;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    vector<int> lvl(n+1, 1e9);
    vector<int> parent(n+1, 0);
    queue<pair<int, int>> q;
    q.push({1, 0});

    vector<int> bfs(n);
    for (auto &x : bfs) cin >> x;

    while (!q.empty()) {
        auto [x,cur_lvl] = q.front(); q.pop();

        lvl[x] = cur_lvl;
        for (auto y : adj[x]) {
            if (lvl[y] < 1e9) continue;

            parent[y] = x;
            q.push({y, cur_lvl+1});
        }
    }

    vector<int> pos(n + 1);
    for (int i = 0; i < n; i++) pos[bfs[i]] = i;

    bool ans = (bfs[0] == 1);
    for (int i = 1; i < n; i++) {
        // cout << "debug: " << bfs[i] << ' ' << lvl[bfs[i]] << '\n'; 
        if (lvl[bfs[i]] < lvl[bfs[i-1]] || pos[parent[bfs[i]]] < pos[parent[bfs[i-1]]]) {
            ans = false;
            break;
        }
    }

    if (ans) cout << "Yes\n";
    else cout << "No\n";
}