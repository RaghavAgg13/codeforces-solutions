#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<int> p,d,parent;

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
        p.resize(n+1); d.resize(n+1);

        for (int i = 1; i <= n; i++) cin >> p[i];
        for (int i = 1; i <= n; i++) cin >> d[i];

        parent.assign(n+1, -1);

        for (int i = 1; i <= n; i++) {
            merge(p[i], i);
        }

        int nos = 0;
        vector<int> vis(n+1, 0);
        for (int i = 1; i <= n; i++) {
            if (!vis[find(p[d[i]])]) {
                nos += -parent[find(p[d[i]])];
                vis[find(p[d[i]])] = 1;
            }
            cout << nos << ' ';
        }   
        cout << '\n';
    }
}