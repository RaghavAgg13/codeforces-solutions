#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
#define ll long long
const int MOD = (int)1e9+7;

int t,n,m,a,b;
vector<int> dsu;

int find(int x) {
    while (dsu[x] > 0) {
        while (dsu[dsu[x]] > 0) dsu[x] = dsu[dsu[x]];
        x = dsu[x];
    }

    return x;
}

void merge(int x, int y) {
    x = find(x);
    y = find(y);

    if (x == y) return;

    if (dsu[x] <= dsu[y]) {
        dsu[x] += dsu[y];
        dsu[y] = x;
    } else {
        dsu[y] += dsu[x];
        dsu[x] = y;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> a(n), b(n), d(n);
        dsu.assign(n+1, -1);
        
        for (auto &x : a) cin >> x;
        for (auto &x : b) cin >> x;
        for (auto &x : d) cin >> x;

        for (int i = 0; i < n; i++) {
            merge(a[i], b[i]);
        }

        unordered_map<int, int> map;
        for (int i = 0; i < n; i++) {
            if (d[i]) map[find(d[i])] = 1;
        }

        ll ways = 1;
        for (int i = 1; i <= n; i++) {
            if (map[find(i)]) continue;
            map[find(i)] = 1;

            if (dsu[find(i)] < -1) ways = (ways*2LL)%MOD;
        }
        cout << ways << '\n';
    }
}