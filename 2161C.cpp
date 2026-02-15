#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int t;
    cin >> t;

    int n,x;
    while (t--) {
        cin >> n >> x;
        vector<int> arr(n), ans(n);

        for (auto &x : arr) cin >> x;
        sort(arr.begin(), arr.end());

        ll bonus = 0, cost = 0;
        int idx = 0, l = 0, r = n-1;
        while (l <= r) {
            if ((cost+arr[r])/x > cost/x) {
                bonus += arr[r];
                
                ans[idx++] = arr[r];
                
                cost += arr[r--];
            }
            else {
                ans[idx++] = arr[l];
                cost += arr[l++];
            }
            
        }

        cout << bonus << '\n';
        for (auto &x: ans) cout << x << ' ';
        cout << '\n';
    }
}