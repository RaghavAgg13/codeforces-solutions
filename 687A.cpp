#include <iostream>
#include <vector>
#include <stack>
using namespace std;
#define ll long long

int n, m, a,b;
vector<vector<int>> adj;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    stack<int> s;

    cin >> n >> m;
    vector<int> visited(n+1, false), color(n+1, -1), gp1, gp2;
    adj.resize(n+1, vector<int>());

    while (m--) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    bool bk = false;

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            visited[i] = 1;
            color[i] = 0;
            s.push(i);
        }

        while (!s.empty()) {
            int cur = s.top();
            s.pop();

            for (auto x : adj[cur]) {
                if (color[x] == color[cur]) {
                    bk = true;
                    break;
                }

                if (!visited[x]) {
                    visited[x] = 1;
                    color[x] = 1-color[cur];
                    s.push(x);
                }
            }
            if (bk) break;
        }
        if (bk) break;
    }

    for (int i = 1; i <= n; i++) {
        if (color[i] == 0) gp1.push_back(i);
        else gp2.push_back(i);
    }

    if (bk) cout << -1;
    else {
        cout << gp1.size() << '\n';
        for (auto x : gp1) cout << x << ' ';
        cout << '\n' << gp2.size() << '\n';
        for (auto x : gp2) cout << x << ' ';
        cout << '\n';
    }

}