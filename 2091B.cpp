#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int t;
    cin >> t;

    int n,x;
    while (t--) {
        cin >> n >> x;
        vector<int> arr(n);

        for (auto &x : arr) cin >> x;
        sort(arr.begin(), arr.end());

        int cnt = 0, freq = 0;
        for (int i = n-1; i >= 0; i--) {
            freq++;
            if (arr[i]*freq >= x) {
                cnt++; 
                freq = 0;
            }
        }

        cout << cnt << '\n';
    }
}