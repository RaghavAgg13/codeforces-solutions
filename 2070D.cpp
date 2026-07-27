#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define ll long long
#define MOD 998244353

int t,n,m,a;
ll ans;
vector<vector<int>> adj;
vector<ll> cnt;

void dfs(int x, int depth, ll ways) {
    for (auto y : adj[x]) {
        // 'ways' ways incoming into this node (will be the same for each node on the same level)
        // ways*cnt[depth] leaving this node (all nodes on this lvl), for each node on next lvl.
        // so each node on nxt lvl get ways*cnt[depth] ways.

        int n_ways = depth == 0 ? 1 : (ways*(cnt[depth]-1))%MOD;
        ans = (ans+n_ways)%MOD;
        dfs(y, depth+1, n_ways);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n+1 , vector<int>());
        cnt.clear();

        for (int i = 2; i <= n; i++) {
            cin >> a;
            adj[a].push_back(i);
        }

        queue<int> q;
        q.push(1);

        while (!q.empty()) {
            int sz = q.size();
            cnt.push_back(sz);

            while (sz--) {
                auto x = q.front(); q.pop();

                for (auto y : adj[x]) {
                    q.push(y);
                }
            }
        }

        ans = 1;
        dfs(1, 0, 1);

        cout << ans << '\n';
    }
}