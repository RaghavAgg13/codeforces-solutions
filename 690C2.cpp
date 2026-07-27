#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;

void dfs(int x, int par, int depth) {
    if (depth > b) {
        a = x;
        b = depth;
    }

    for (auto y : adj[x]) {
        if (y == par) continue;
        dfs(y, x, depth+1);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.assign(n+1, vector<int>());

    while (m--) {
        cin >> a >> b;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    a = -1, b = 0;
    dfs(1, -1, 0);

    m = a;
    a = -1, b = 0;
    dfs(m, -1, 0);

    cout << b << '\n';
}