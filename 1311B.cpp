#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> m;
        vector<int> arr(n);
        for (auto &x : arr) cin >> x;
        
        vector<int> p(n, 0);
        while (m--) {
            cin >> a;
            p[a] = 1;
        }

        bool s = true;
        while (s) {
            s = false;
            for (int i = 1; i < n; i++) {
                if (arr[i-1] > arr[i] && p[i]) {
                    swap(arr[i-1], arr[i]);
                    s = true;
                }
            }

            if (!s) break;
        }

        vector<int> b(arr.begin(), arr.end());
        sort(b.begin(), b.end());

        s = true;
        for (int i = 0; i < n; i++) {
            if (arr[i] != b[i]) {
                s = false;
                 break;
            }
        }

        if (s) cout << "YES\n";
        else cout << "NO\n";
    }
    
}