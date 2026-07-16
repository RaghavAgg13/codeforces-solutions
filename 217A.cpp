#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int n,m,a,b;
vector<int> pts, vis;
vector<vector<int>> adj;
unordered_map<int, int> map;

void dfs(int i) {
    vis[i] = 1;

    for (auto x : adj[i]) {
        if (!vis[x]) dfs(x);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());
    
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        pts.emplace_back(a*1000+b);
        map[a*1000+b] = i;
    }

    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            int ax = pts[i]/1000, ay = pts[i]%1000;
            int bx = pts[j]/1000, by = pts[j]%1000;

            if (ax == bx || ay == by) {
                adj[i].push_back(j);
                adj[j].push_back(i);
            }
        }
    }

    vis.assign(n+1, 0);
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (vis[i]) continue;
        
        dfs(i);
        cnt++;
    }
    
    cout << cnt-1 << '\n';
}