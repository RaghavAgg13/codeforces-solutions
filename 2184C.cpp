#include <bits/stdc++.h>
using namespace std;

int solve(int n, int k) {
    if (k == n) return 0;

    int time = 0, gap = 1;
    while (k < n) {
        time += 1;
        k = k*2-1;
        gap = gap*2+1;

        // cout << "time, k, gap" << time << k << gap << '\n';

        if (k+gap > n && n >= k) return time;
    }

    return -1;
}

int main(void) {
    int t;
    cin >> t;

    while (t--) {
        int n,k;
        cin >> n >> k;

        int a = solve(n, k);
        cout << a << '\n';
    }
}

