#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
 
int t,n;
 
int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> arr(n);
        for (auto &x: arr) cin >> x;

        int l = 0, r = n-1;
        int coins = 0;


        while (l <= r) {
            if (r && arr[r-1] == 1) { r--; }
            if (l<n && arr[l+1] == 1) { l++; }

            if (r && l < n && arr[l+1] != 1 && arr[r-1] != 1) break;

            // cout << "debug " << l << ' ' << r << endl;
        }

        // if (n == 2) cout << "2\n";
        cout << max(r-l, 0)+coins << endl;
    }    
}