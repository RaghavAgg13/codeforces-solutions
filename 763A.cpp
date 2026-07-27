#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;
vector<int> color;
vector<pair<int, int>> edges;

bool check(int x, int p) {
    bool ans = true;
    for (auto y : adj[x]) {
        if (y == p) continue;

        if (color[x] != color[y] || !check(y,x)) return false;
    }
    return true;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());
    color.resize(n+1);
    edges.clear();

    m = n; while (--m) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
        edges.push_back({a,b});
    }

    for (int i = 1; i <= n; i++)  cin >> color[i];

    int root1 = -1, root2 = -1;
    for (auto [u, v] : edges) {
        if (color[u] != color[v]) {
            root1 = u;
            root2 = v;
            break;
        }
    }

    if (root1 == -1) {
        cout << "YES\n1";
        return 0;
    }

    bool chk1 = true, chk2 = true;
    for (auto x : adj[root1]) {
        if (!check(x, root1)) {
            chk1 = false;
            break;
        }
    }

    if (chk1) {
        cout << "YES\n" << root1 << '\n';
        return 0;
    }

    for (auto x : adj[root2]) {
        if (!check(x, root2)) {
            chk2 = false;
            break;
        }
    }

    if (chk2) cout << "YES\n" << root2 << '\n';
    else cout << "NO";
}