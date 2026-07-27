#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,k,a,b,non_gov;
vector<vector<int>> adj,grps;
vector<int> vis,gov;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;
    adj.assign(n+1, vector<int>());
    grps.assign(n+1, vector<int>());
    vis.assign(n+1, 0);
    gov.assign(n+1, 0);

    for (int i = 1; i <= k; i++) {
        cin >> a;
        gov[a]++;
    }

    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    queue<int> q;
    for (int i = 1; i <= n; i++) {
        if (!gov[i] || vis[i]) continue;
        vis[i] = 1;
        q.push(i);

        while (!q.empty()) {
            auto x = q.front(); q.pop();
            grps[i].push_back(x);
            
            for (auto y : adj[x]) {
                if (vis[y]) continue;
                vis[y] = 1;

                q.push(y);
            }
        }
    }

    // all non-gov connects themselves nc2 and they connect once to a gov
    // for each group now, the max edges = (#non-gov, 2)ncr + #non-gov
    
    int idx = 1;
    for (int i = 1; i <= n; i++) {
        if (gov[i] && grps[i].size() > grps[idx].size()) idx = i;
    }
   
    for (int i = 1; i <= n; i++) {
        if (!vis[i]) grps[idx].push_back(i);
    }

    b = 0;
    for (int i = 1; i <= n; i++) {
        a = grps[i].size();
        b += (a*(a-1))/2;
    }

    cout << b-m;
}