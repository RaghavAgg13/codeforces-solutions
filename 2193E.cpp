#include <bits/stdc++.h>
using namespace std;
#define ll long long

int n, t, tmp;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> freq(n+1, 0);
        vector<int> dp(n+1, 1e9);

        for (int i = 0; i < n; i++) {
            cin >> tmp;
            if (tmp <= n) freq[tmp]++;
        }

        for (int i = 1; i <= n; i++) {
            if (freq[i]) dp[i] = 1; 

            if (dp[i] == 1e9) cout << -1 << ' ';
            else cout << dp[i] << ' ';

            if (dp[i] != 1e9) {
                for (int j = 2 * i; j <= n; j += i) {
                    int multiplier = j/i;
                    if (freq[multiplier]) {
                        dp[j] = min(dp[j], dp[i]+1);
                    }
                }
            }
        }
        cout << endl;
    }
}