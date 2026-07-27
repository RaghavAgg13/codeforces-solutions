#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
#define ll long long

int n,m,a,b;
vector<int> x,y,dsu;

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

    cin >> n;
    dsu.assign(n+1, -1);

    x.resize(n); y.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> x[i];
        y[i] = x[i];
    }

    sort(y.begin(), y.end());

    unordered_map<int, int> map;
    vector<vector<int>> grps(n+1, vector<int>());

    for (int i = 0; i < n; i++) map[y[i]] = i;
    
    for (int i = 0; i < n; i++) {
        merge(map[x[i]], map[y[i]]);
    }
    
    for (int i = 0; i < n; i++) {
        grps[find(map[x[i]])].push_back(i);
    }

    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (!grps[i].size()) continue;
        cnt++;
    }

    cout << cnt << '\n';
    for (int i = 0; i < n; i++) {
        if (!grps[i].size()) continue;
        
        cout << grps[i].size() << ' ';
        for (auto &x : grps[i]) cout << x+1 << ' ';
        cout << '\n';
    }
}