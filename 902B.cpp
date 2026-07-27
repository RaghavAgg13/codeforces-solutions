#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj, tree;
vector<int> color;

void dfs(int x, int par) {
    for (auto y : adj[x]) {
        if (y == par) continue;
        tree[x].push_back(y);

        dfs(y, x);
    }
} 

void set(int x, int col) {
    for (auto y : tree[x]) {
        if (color[y] == col) {
            set(y, col);
        } else {
            b += 1;
            set(y, color[y]);
        }
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    color.resize(n+1);
    adj.resize(n+1, vector<int>());
    tree.resize(n+1, vector<int>());

    for (int i = 2; i <= n; i++) {
        cin >> a;
        adj[a].push_back(i);
        adj[i].push_back(a);
    }
    
    for (int i = 1; i <= n; i++) {
        cin >> a; color[i] = a;
    }

    dfs(1, -1);

    b = 1;
    set(1, color[1]);

    cout << b;
}
