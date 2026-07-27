#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#define ll long long
using namespace std;

ll t,n,m,b;
vector<ll> arr,a;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        arr.resize(n);
        a.resize(n);

        for (auto &x : arr) cin >> x;
    
        for (int i = 0; i < n; i++) {
            a[i] = arr[i]+i;
        }

        map<ll, vector<ll>> map;
        for (int i = 1; i < n; i++) {
            map[a[i]].push_back(a[i]+i);
        }

        queue<ll> q;
        q.push(n);

        while (!q.empty()) {
            auto x = q.front(); q.pop();

            if (!map.count(x)) continue;
            for (auto &y : map[x]) {
                n = max(n, y);
                if (map.count(y)) q.push(y);
            }
            map.erase(x);
        }

        cout << n << '\n';
    }
}