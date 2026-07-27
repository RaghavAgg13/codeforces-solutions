#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long

int n,m,k,a,b;
ll ans = 0;
vector<vector<int>> adj,dp;

void dfs(int x, int par) {
    dp[x][0] = 1;

    for (auto y : adj[x]) {
        if (y == par) continue;
        dfs(y, x);

        for (int d = 1; d <= k; d++) {
            ans += 1LL*dp[x][d-1]*dp[y][k-d];
        }

        for (int d = 1; d <= k; d++) dp[x][d] += dp[y][d-1];
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> k;
    adj.assign(n+1, vector<int>());
    dp.resize(n+1, vector<int>(k+1));

    m = n; while (--m) {
        cin >> a >> b;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(1, -1);
    cout << ans << '\n';
}