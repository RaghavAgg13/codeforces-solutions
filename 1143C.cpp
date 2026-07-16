#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,a,b,parent;
vector<vector<int>> adj;
vector<int> c,sp,no;

void dfs(int root) {
    sp[root] = c[root];

    for (auto x : adj[root]) {
        dfs(x);
        sp[root] *= c[x];
    }

    if (sp[root]) no.push_back(root);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());
    c.resize(n+1);
    sp.assign(n+1, 0);

    for (int i = 1; i <= n; i++) {
        cin >> a >> b;
        c[i] = b;

        if (a == -1) parent = i;
        else adj[a].push_back(i);
    }

    no.clear();
    dfs(parent);

    sort(no.begin(), no.end());
    if (!no.size()) {
        cout << "-1\n";
        return 0;
    }

    for (auto x : no) cout << x << ' ';
}