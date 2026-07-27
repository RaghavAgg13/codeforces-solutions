#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long

int t,n,m1,m2,a,b;
vector<pair<int, int>> edges,edges2;

int find(int x, vector<int> &dsu) {
    if (dsu[x] < 0) return x;
    return dsu[x] = find(dsu[x], dsu);
}

void merge(int x, int y, vector<int> &dsu) {
    x = find(x, dsu);
    y = find(y, dsu);

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

    cin >> t;
    while (t--) {
        cin >> n >> m1 >> m2;
        vector<int> dsu(n+1, -1), dsu2(n+1, -1);
        edges.clear();
        edges2.clear();
        
        while (m1--) {
            cin >> a >> b;
            edges.push_back({a,b});
        }
        
        while (m2--) {
            cin >> a >> b;
            edges2.push_back({a,b});
            merge(a,b, dsu);
        }
    
        b = 0;
        for (auto edge : edges) {
            if (find(edge.first, dsu) != find(edge.second, dsu)) b++;
            else merge(edge.first, edge.second, dsu2);
        }
        for (auto edge : edges2) {
            if (find(edge.first, dsu2) != find(edge.second, dsu2)) {
                b++;
                merge(edge.first, edge.second, dsu2);
            }
        }

       cout << b << '\n';
    }
}