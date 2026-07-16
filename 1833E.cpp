#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,a,b;
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
        parent.resize(n+1);
        for (int i = 1; i <= n; i++) parent[i] = -1;

        vector<int> in(n+1, 0);
        int cnt = n;

        for (int i = 1; i <= n; i++) {
            cin >> a;
            in[a]++;

            if (find(a) != find(i)) {
                merge(a, i);
                cnt--;
            }
        }

        vector<int> open(n+1, 0);
        for (int i = 1; i <= n; i++) {
            if (in[i] != 1) {
                open[find(i)] = 1;
            }
        }

        b = 0;
        for (int i = 1; i <= n; i++) {
            if (i == find(i)) {
                if (parent[i] == -2) {
                    open[i] = 1;
                }

                if (!open[i]) b++;
            }
        }

        cout << b+min(cnt-b,1) << ' ' << cnt << '\n';
    }
    
}