#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
using namespace std;
#define ll long long

int t,n,m,a,b;
ll ans;
vector<ll> arr, ss;
vector<vector<int>> adj;

void dfs(int x, int parent) {
    vector<ll> val;

    for (auto y: adj[x]) {
        if (y == parent) continue;
        dfs(y, x);
        val.push_back(ss[y]);
        ss[x] += ss[y];
    }

    val.push_back(n-ss[x]);
    if ((ll)sqrtl(arr[x])*(ll)sqrtl(arr[x]) < arr[x]) return;

    ll sum = 0, pairs = 0, triplets = 0;
    for (auto &z : val) {
        triplets += pairs*z;
        pairs += sum*z;
        sum += z;
    }

    ans += pairs+triplets;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        arr.assign(n, 0);
        for (auto &x : arr) cin >> x;

        adj.assign(n, vector<int>());
        m = n; while (--m) {
            cin >> a >> b;
            a--; b--;

            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        ans = 0;
        ss.assign(n, 1);
        dfs(0, -1);

        cout << ans << '\n';
    }
}