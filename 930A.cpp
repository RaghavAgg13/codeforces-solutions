#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;
vector<int> val;

void dfs(int x, int depth) {
    val[depth] ^= 1;

    for (auto y : adj[x]) {
        dfs(y, depth+1);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());
    val.assign(n+1, 0);

    for (int i = 2; i <= n; i++) {
        cin >> a;
        adj[a].push_back(i);
    }
    
    b = 0;
    dfs(1, 0);

    for (int i = 0; i <= n; i++) b += val[i];

    cout << b;
}