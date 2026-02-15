#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
 
ll t,n,m,k;
 
int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> m >> k;

        ll l = 0, r = min(k-1, n-k);
        ll cost = 0;
        while (l <= r) {
            ll mid = l+(r-l)/2;
            ll req = (mid == 0) ? 0 : 3 * mid - 1;

            if (req <= m) {
                cost = mid;
                l = mid+1;
            } else r = mid-1;
        }

        ll ans = 1+ 2*cost;
        m -= (cost == 0) ? 0 : 3 * cost - 1;
        ll extra = 0;

        if (cost < min(k-1, n-k)) {
            if (m >= ((cost == 0) ? 1 : 2)) ans++;
        }
        else {
            ll rem_space = abs(n-k - (k-1));
            ll affordable = 0;

            if (cost == 0) {
                if (m > 0) affordable = (m + 1) / 2;
            } else affordable = m / 2;

            ans += min(rem_space, affordable);
        }
        cout << ans << endl;
    }    
}