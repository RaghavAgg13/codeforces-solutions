#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<int> arr(n);

    cin >> arr[0];
    for (int i = 1; i < n; i++) {
        cin >> arr[i];
        arr[i] += arr[i-1];
    }

    int q, x;
    cin >> q;
    for (int i = 0; i < q; i++) {
        cin >> x;

        int l = 0, r = n-1;
        int mid;
        while (l < r) {
            mid = l + (r-l)/2;

            if (arr[mid] < x) l = mid+1;
            else r = mid;
        }

        cout << r+1 << endl;
    }
}