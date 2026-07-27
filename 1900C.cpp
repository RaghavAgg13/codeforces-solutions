#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int t,n,m,a,b;
string s;
vector<pair<int, int>> adj;
vector<int> val;

void get(int x, int cost) {
    if (adj[x].first == 0 && adj[x].second == 0) {
        b = min(b, cost);
        return;
    }

    if (adj[x].first) {
        int add = (s[x] != 'L') ? 1 : 0;
        get(adj[x].first, cost+add);
    }
    if (adj[x].second) {
        int add = (s[x] != 'R') ? 1 : 0;
        get(adj[x].second, cost+add);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        cin >> s; s = " "+s;
        adj.resize(n+1, pair<int, int>());

        for (int i = 1; i <= n; i++) {
            cin >> a >> b;
            adj[i] = {a,b};
        }

        val.assign(n+1, 0);
        b = 10000000;
        get(1, 0);

        cout << b << '\n';
    }
}