#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int n,m,a,b;
vector<int> dsu,sz;

int find(int x) {
    while (dsu[x] > 0) {
        while (dsu[dsu[x]] > 0) dsu[x] = dsu[dsu[x]];
        x = dsu[x];
    }

    return x;
}

void merge(int x, int y) {
    x = find(x);
    y = find(y);

    if (x == y) return;

    if (dsu[x] <= dsu[y]) {
        dsu[x] += dsu[y];
        dsu[y] = x;
    } else {
        dsu[y] += dsu[x];
        dsu[x] = y;
    }
}


int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    sz.assign(n+1, 0);
    dsu.assign(n+1, -1);

    while (m--) {
        cin >> a >> b;
        sz[a]++; sz[b]++;
        merge(a, b);
    }

    vector<vector<int>> grps(n+1, vector<int>());
    set<int> par;
    for (int i = 1; i <= n; i++) {
        par.insert(find(i));
        grps[find(i)].push_back(i);
    }

    a = 0;
    for (auto p : par) {
        bool pos = true;
        for (auto items : grps[p]) {
            if (sz[items] != 2) {
                pos = false;
                break;
            }
        }
        if (pos) a++;
    }    
    cout << a;
}