#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,a;
vector<int> parent;

int find(int u) {
    while (parent[u] >= 0) {
        if (parent[parent[u]] >= 0) parent[u] = parent[parent[u]];
        u = parent[u];
    }

    return u;
}

void merge(int u, int v) {
    u = find(u); v = find(v);

    if (u == v) return;

    if (parent[u] <= parent[v]) {
        parent[u] += parent[v];
        parent[v] = u;
    } else {
        parent[v] += parent[u];
        parent[u] = v;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        parent.assign(n+1, -1);

        for (int i = 1; i <= n; i++) {
            cin >> a;
            merge(i, a);
        }

        for (int i = 1; i <= n; i++) {
            cout << -parent[find(i)] << ' ';
        }
        cout << '\n';
    }
    
}