#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n;
vector<int> arr;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        arr.resize(n);
        
        for (auto &x : arr) cin >> x;

        bool pos = true;
        int lvl = 0;
        for (int gap = 1; (1<<gap) <= n; gap++) {
            int k = 1<<(gap-1);

            for (int i = k; i < n; i += 2*k) {
                if (arr[i]+k == arr[i-k]) {
                    arr[i-k] = arr[i];
                    lvl++;
                }
                else if (arr[i] == arr[i-k]+k) continue;
                else {
                    pos = false;
                    break;
                }
            }
            if (!pos) break;
        }

        if (!pos) cout << "-1\n";
        else cout << lvl << '\n';
    } 
}