#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#define ll long long
using namespace std;

int n,m,a,b;
double pr;
vector<vector<int>> adj;

void dfs(int root, int parent, double p, int depth) {
    if (adj[root].size() == 1) {
        pr += (double)depth*p;
        return;
    }

    for (auto x : adj[root]) {
        if (x == parent) continue;

        int s = adj[root].size()-1;
        dfs(x, root, p/s, depth+1);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());
    
    m = n; while(--m) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    adj[1].push_back(-1);
    dfs(1, -1, 1.0, 0);

    cout << fixed << setprecision(15) << pr << '\n';
}