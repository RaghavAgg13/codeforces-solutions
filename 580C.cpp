#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;
vector<int> cat;

int recur(int root, int cats, int parent) {
    if (cat[root]) cats++;
    else cats = 0;
    if (cats > m) return 0;
    if (root != 1 && adj[root].size() == 1) return 1;

    int cnt = 0;
    for (auto x : adj[root]) {
        if (x == parent) continue;    
        cnt += recur(x, cats, root);
    }

    return cnt;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.resize(n+1, vector<int>());
    cat.resize(n+1, 0);

    for (int i = 1; i <= n; i++) cin >> cat[i];

    while (--n) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    cout << recur(1, 0, -1) << '\n';
    
}