#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define ll long long
#define MOD 998244353

int t,n,m,a,b;
vector<ll> cnt;
vector<int> depth;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        depth.assign(n+1, 0);
        cnt.assign(n+1, 0);

        cnt[0] = 1;
        m = 0;

        for (int i = 2; i <= n; i++) {
            cin >> a;
            depth[i] = depth[a]+1;
            cnt[depth[i]]++;
            m = max(m, depth[i]);
        }

        ll dp = 1, ans = 1;

        for (int i = 1; i <= m; i++) {
            dp = dp*(i == 1 ? 1 : cnt[i-1]-1);
            dp %= MOD;

            ans = (ans+dp*cnt[i])%MOD;
        }

        cout << ans << '\n';
    }
}