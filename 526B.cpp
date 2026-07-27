#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<pair<int, int>>> adj;

int dfs(int x, int lamps) {
    if (adj[x].size() == 0) return 0;

    int l = dfs(adj[x][0].first, 0)+adj[x][0].second, r = dfs(adj[x][1].first, 0)+adj[x][1].second;

    b += abs(l-r);
    return max(l,r);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    m = (1<<(n+1))-2;
    adj.assign(m+2, vector<pair<int, int>>());

    for (int i = 2; i <= m+1; i++) {
        cin >> a;
        adj[i/2].push_back({i, a});
    }
    
    b = 0;
    dfs(1, 0);
    cout << b;
}