#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj, adj_;
vector<int> init, goal, x_i;

void root(int x, int par) {
    for (auto y : adj_[x]) {
        if (y == par) continue;

        adj[x].push_back(y);
        root(y, x);
    }
}

void solve(int x, int cur, int next) {
    if (cur) init[x] = 1-init[x];

    if (init[x] != goal[x]) {
        b += 1;
        x_i.push_back(x);
        cur = 1-cur;
    }
    for (auto y : adj[x]) solve(y, next, cur);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());
    adj_.assign(n+1, vector<int>());

    m = n; while (--m) {
        cin >> a >> b;
        adj_[a].push_back(b);
        adj_[b].push_back(a);
    }
    
    root(1, -1);

    init.assign(n+1, 0); goal.assign(n+1, 0);

    for (int i = 1; i <= n; i++) cin >> init[i];
    for (int i = 1; i <= n; i++) cin >> goal[i];

    b = 0;
    x_i.clear();
    
    solve(1, 0, 0);

    cout << b;
    for (auto x : x_i) cout << '\n' << x;
}