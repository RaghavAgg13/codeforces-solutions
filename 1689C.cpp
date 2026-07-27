#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<vector<int>> adj;
vector<int> sub_size;

void get(int x, int p) {
    int c = 0, mn = 1e9;
    for (auto y : adj[x]) {
        if (y == p) continue;

        get(y, x);
        c++;
        mn = min(mn, sub_size[y]);
    }

    if (c == 0) sub_size[x] = 1;
    else if (c == 1) sub_size[x] = 2;
    else sub_size[x] = 2+mn;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n+1, vector<int>());
        sub_size.assign(n+1, 0);

        m = n; while (--m) {
            cin >> a >> b;
            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        get(1, -1);

        cout << n-sub_size[1] << '\n';
    }
}