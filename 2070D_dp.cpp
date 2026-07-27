#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define ll long long
#define MOD 998244353

int t,n,m,a,b;
vector<vector<int>> adj;
vector<ll> cnt;

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

        queue<int> q; q.push(1);

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
        m = cnt.size();

        ll dp[m] = {1};
        ll ans = 1;

        for (int i = 1; i < m; i++) {
            dp[i] = dp[i-1]*(i == 1 ? 1 : cnt[i-1]-1);
            dp[i] %= MOD;

            ans = (ans+dp[i]*cnt[i])%MOD;
        }

        cout << ans << '\n';
    }
}