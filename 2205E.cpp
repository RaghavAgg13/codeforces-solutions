#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define MOD 998244353

int n, t, tmp;
int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> arr(n);
        for (auto &x : arr) cin >> x;

        vector<int> dp(n+1, 0);
        dp[0] = 1;

        for (int j = 0; j < n; j++) {
            if (dp[j] == 0) continue;

            vector<int> pi(n-j, 0);
            int k = 0;

            dp[j+1] = (dp[j+1]+dp[j])%MOD;

            for (int i = 1; i < n-j; i++) {
                while (k > 0 && arr[i+j] != arr[j+k]) k = pi[k-1];
                if (arr[i+j] == arr[j+k]) k++;
                pi[i] = k;

                if (!k) dp[i+j+1] = (dp[i+j+1]+dp[j])%MOD;
            }
        }

        cout << dp[n] << '\n';
    }
}