#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<vector<int>> adj;
vector<int> leaves;

int dfs(int root, int parent) {
    leaves[root] = 0;
    if (root != 1 && adj[root].size() == 1) leaves[root]++;

    for (auto x : adj[root]) {
        if (x == parent) continue;

        dfs(x, root);
        leaves[root] += leaves[x];
    }

    return leaves[root];
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n+1, vector<int>());
        leaves.assign(n+1, 0);

        m = n; while(--m) {
            cin >> a >> b;

            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        dfs(1, -1);

        cin >> m;
        while (m--) {
            cin >> a >> b;
            cout << 1LL*leaves[a]*leaves[b] << '\n'; 
        }
    }
    
}