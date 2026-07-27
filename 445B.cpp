#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
#define ll long long

int n,m,a,b;
vector<int> dsu;

int find(int x) {
    if (dsu[x] < 0) return x;
    return dsu[x] = find(dsu[x]);
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
    dsu.assign(n+1, -1);
    
    while (m--) {
        cin >> a >> b;

        merge(a,b);
    }

    unordered_map<int, int> map;
    vector<int> finals;
    for (int i = 1; i <= n; i++) {
        if (!map[find(i)]) {
            finals.push_back(find(i));
            map[find(i)] = 1;
        }
    }

    ll danger = 1;
    for (auto x : finals) {
        ll size = -dsu[x]-1;
        danger *= (1LL << size);
    }
    cout << danger;
}