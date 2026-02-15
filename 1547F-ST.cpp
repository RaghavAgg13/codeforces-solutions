// #include <bits/stdc++.h>
#include <vector>
#include <math.h>
#include <iostream>
using namespace std;
#define ll long long

class sparseTable {
    vector<vector<int>> st;
    vector<int> logs;
    int N,K_log;

public:
    sparseTable(const vector<int> &arr) {
        N = arr.size();
        K_log = log2(N)+1;
        
        st.assign(N, vector<int>(K_log));
        logs.assign(N+1, 0);

        // preCompute logs - optmization
        for (int i = 2; i <= N; ++i) logs[i] = logs[i/2]+1;

        // create sparse table by dp
        for (int i = 0; i < N; ++i) st[i][0] = arr[i];

        for (int j = 1; j < K_log; ++j) {
            for (int i = 0; i+(1<<j) <= N; ++i) {
                st[i][j] = gcd(st[i][j-1], st[i+(1<<(j-1))][j-1]);
            }
        }
    }

    bool checkUniform(int windowSize) {
        int k = logs[windowSize];
        int numWindows = N - windowSize + 1;
        
        int targetGCD = gcd(st[0][k], st[windowSize - (1 << k)][k]);
        
        for (int i = 1; i < numWindows; i++) {
        int currentGCD = gcd(st[i][k], st[i + windowSize - (1 << k)][k]);
        if (currentGCD != targetGCD) return false;
    }
        return true;
    }
};

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int t, n;
    cin >> t;

    while (t--) {
        cin >> n;
        vector<int> a(n);
        for (auto &it : a) cin >> it;

        vector<int> extended_a = a;
        extended_a.insert(extended_a.end(), a.begin(), a.end());

        sparseTable table(extended_a);

        int l = 1, r = n;
        int ans = n;
        
        while (l <= r) {
            int mid = l + (r-l)/2;

            if (table.checkUniform(mid)) {
                ans = mid;
                r = mid-1;
            } else l = mid+1;
        }

        cout << ans-1 << endl;
    }
    return 0;
}