#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int n,m,a,b;
vector<int> parent;

int find(int u) {
    while (parent[u] >= 0) u = parent[u];

    return u;
}

void merge(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;

    if (parent[a] >= parent[b]) {
        parent[b] += parent[a];
        parent[a] = b;
    }
    else {
        parent[a] += parent[b];
        parent[b] = a;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    parent.assign(n+1, -1);

    while (m--) {
        cin >> a;

        int first = -1;
        while (a--) {
            cin >> b;

            if (first == -1) first = b;
            else merge(first, b);
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << -parent[find(i)] << ' ';
    }
}