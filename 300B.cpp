#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b,c;
vector<vector<int>> adj,comp[4];
vector<int> vis;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.assign(n+1, vector<int>());
    vis.assign(n+1, 0);

    while (m--) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    
    for (int i = 1; i < 4; i++) comp[i].clear();

    for (int i = 1; i <= n; i++) {
        if (vis[i]) continue; vis[i] = 1;
        vector<int> tmp;
        
        queue<int> q({i});
        while (!q.empty()) {
            auto x = q.front(); q.pop();

            tmp.push_back(x);

            for (auto y : adj[x]) {
                if (vis[y]) continue; vis[y] = 1;

                q.push(y);
            } 
        }

        if (tmp.size() > 3) {
            cout << -1;
            return 0;
        }
        else if (tmp.size() == 3) comp[3].push_back(tmp);
        else if (tmp.size() == 2) comp[2].push_back(tmp);
        else comp[1].push_back({tmp[0]});
    }

    if (comp[2].size() > comp[1].size()) {
        cout << -1;
        return 0;
    }

    b = 0, c = 0;
    for (auto& team : comp[2]) {
        team.push_back(comp[1].back()[0]);
        comp[1].pop_back();
        comp[3].push_back(team);
    }

    for (auto y : comp[3]) {
        for (auto x : y) cout << x << ' ';
        cout << '\n';
    }

    b = 0;
    while (c < comp[1].size()) {
        cout << comp[1][c++][0] << ' ';
        if ((++b)%3 == 0) cout << '\n';
    }
}