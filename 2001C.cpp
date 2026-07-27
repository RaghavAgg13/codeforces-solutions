#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <unordered_map>
using namespace std;

int t,n,m,b,cnt;
set<int> edges;
vector<int> vis;
unordered_map<int, int> processed;

void solve(int l, int r) {
    int key = min(l,r)*m + max(l,r);
    if (processed[key]) return;
    processed[key] = 1;

    cout << "? " << l << ' ' << r << '\n';
    cout.flush();
    int a; cin >> a;

    if (a == l || a == r) {
        vis[l] = 1;
        vis[r] = 1;
        edges.insert(min(l, r) * m + max(l, r));
        return;
    }

    solve(l, a); solve(a, r);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        m = n+1;
        cnt = 0;
        edges.clear();
        processed.clear();
        vis.assign(n+1, 0);

        for (int i = 1; i < n; i++) {
            if (vis[i]) continue;
            solve(i, n);
        }

        cout << "! ";
        for (auto edge : edges) cout << edge/m << ' ' << edge%m << ' ';
        cout << '\n';
        cout.flush();
    }
}