#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,q,a,b;
vector<vector<int>> adj;
vector<int> order, sub_sz,idx;

void root(int x) {
    idx[x] = order.size();
    order.push_back(x);

    for (auto y : adj[x]) {
        root(y);
        sub_sz[x] += sub_sz[y];
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> q;
    adj.assign(n+1, vector<int>());
    sub_sz.assign(n+1, 1);
    idx.assign(n+1, 1);
    order = {0};

    for (int i = 2; i <= n; i++) {
        cin >> a;
        adj[a].push_back(i);
    }

    root(1);
    
    while (q--) {
        cin >> a >> b;
        if (b > sub_sz[a]) cout << "-1\n";
        else cout << order[idx[a]+b-1] << '\n';
    }
}