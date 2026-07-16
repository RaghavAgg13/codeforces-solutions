#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,k,m,a,b;
vector<vector<int>> adj;
vector<int> depth, w, siz;

void dfs(int root, int d, int parent) {
    depth[root] = d;
    siz[root] = 1;

    for (auto x : adj[root]) {
        if (x != parent) {
            dfs(x, d+1, root);
            siz[root] += siz[x];
        }
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> k;
    adj.assign(n+1, vector<int>());
    depth.assign(n+1, 0); siz.assign(n+1, 0);

    m = n; while (--m) {
        cin >> a >> b;
        
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    
    dfs(1, 0, -1);

    w.clear();
    for (int i = 1; i <= n; i++) {
        w.push_back(depth[i]-siz[i]+1);
    }

    sort(w.begin(), w.end(), greater<int>());

    long long ans = 0;
    for (int i = 0; i < k; i++) ans += w[i];

    cout << ans << '\n';
}