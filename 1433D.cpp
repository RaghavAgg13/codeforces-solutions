#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int t,n,m,a,b;
vector<int> arr;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        arr.assign(n+1, -1);
        for (int i = 1; i <= n; i++) cin >> arr[i];

        bool pos = true;
        unordered_map<int, int> map;
        for (int i = 1; i <= n; i++) {
            if (++map[arr[i]] == n) {
                pos = false;
                break;
            }
        }

        if (pos) cout << "YES\n";
        else {
            cout << "NO\n";
            continue;
        }
        
        int node = 1;
        for (int i = 2; i <= n; i++) {
            if (map[arr[i]] < map[node]) node = i;
        }

        vector<int> res;
        for (int i = 1; i <= n; i++) {
            if (i != node && arr[i] != arr[node]) {
                cout << node << " " << i << '\n';
                res.push_back(i);
            }
        }
        for (int i = 1; i <= n; i++) {
            if (arr[i] == arr[node] and i != node) {
                cout << res[0] << ' ' << i << '\n';
            }
        }
    }
    
}