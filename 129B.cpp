#include <iostream>
#include <vector>
#include <set>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> n >> m;
    vector<int> size(n+1, 0);
    adj.resize(n+1, vector<int>());

    while (m--) {
        cin >> a >> b;
        adj[a].push_back(b); 
        adj[b].push_back(a);

        size[a]++; size[b]++;
    }

    set<int> q;
    for (int i = 1; i <= n; i++) {
        if (size[i] == 1) q.insert(i);
    }

    int levels = 0;
    while (!q.empty()) {
        set<int> nq;

        for (int x : q) {
            size[x]--;

            for (int y : adj[x]) size[y]--;
        }

        for (int x : q) {
            for (int y : adj[x]) {
                if (size[y] == 1) nq.insert(y);
            }
        }

        q = nq;
        levels++;
    }
    cout << levels;
}