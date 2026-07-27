#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int n,m,a,b;
vector<int> dsu;

int find(int x) {
    while (dsu[x] >= 0) {
        while (dsu[dsu[x]] >= 0) dsu[x] = dsu[dsu[x]];
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
    }
    else {
        dsu[y] += dsu[x];
        dsu[x] = y;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> n;
    dsu.assign(n+1, -1);
    unordered_map<int, int> map;

    for (int i = 1; i <= n; i++) {
        cin >> a;

        merge(a, i);
    }
    
    int trees = 0;
    for (int i = 1; i <= n; i++) {
        if (!map[find(i)]) {
            map[find(i)] = 1;
            trees++;
        }
    }

    cout << trees;
}