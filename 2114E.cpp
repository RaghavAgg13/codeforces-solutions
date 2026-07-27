#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long

int t,n,m,a,b;
vector<vector<int>> adj;
vector<ll> p,arr;

void dfs(int x, int par, ll mi, ll ma) {
    ll new_mi = p[x]-max(0LL, ma), new_ma = p[x]-min(0LL, mi);
    arr[x] = new_ma;

    for (auto y : adj[x]) {
        if (y == par) continue;

        dfs(y, x, new_mi, new_ma);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        p.resize(n);
        for (int i = 0; i < n; i++) {
            cin >> a;
            p[i] = a; 
        }

        adj.assign(n, vector<int>());

        m = n; while (--m) {
            cin >> a >> b;
            a--; b--;
            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        arr.resize(n);
        dfs(0, -1, 0, 0);

        for (auto x : arr) cout << x << ' ';
        cout << '\n';
    }
}