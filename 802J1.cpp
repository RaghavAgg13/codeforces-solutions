#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b,c;
vector<vector<pair<int, int>>> adj;

int dfs(int x, int par) {
    int ans = 0;
    for (auto [y,cst] : adj[x]) {
        if (y == par) continue;

        ans = max(ans, dfs(y, x)+cst);
    }
    return ans;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<pair<int, int>>());
    
    m = n; while(--m) {
        cin >> a >> b >> c;
        adj[a].push_back({b,c});
        adj[b].push_back({a,c});
    }

    int ans = dfs(0, -1);
    cout << ans;
}   