#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;

int dfs(int x, int par) {
    int sz = 1;
    for (auto y : adj[x]) {
        if (y == par) continue;

        int c_sz = dfs(y,x);
        if (c_sz%2 == 0) b++;
        else sz += c_sz;
    }

    return sz;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());

    m = n; while (--m) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    if (n%2) {
        cout << -1;
        return 0;
    }

    b = 0;
    dfs(1, -1);
    cout << b << '\n';
}