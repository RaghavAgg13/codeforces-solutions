#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;
#define ll long long

int q,n,m,t,a,b;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    vector<vector<int>> adj(n+1);
    vector<int> degree(n+1, 0), top;

    while (m--) {
        cin >> a >> b;
        adj[b].push_back(a);
        degree[a]++;
    }

    priority_queue<int> Q;
    for (int i = 1; i <= n; i++) {
        if (!degree[i]) Q.push(i);
    }

    while(!Q.empty()) {
        auto cur = Q.top(); Q.pop();
        top.push_back(cur);

        for (auto x : adj[cur]) {
            if (--degree[x] == 0) Q.push(x);
        }
    }

    unordered_map<int, int> map;
    int cnt = n;
    for (auto x : top) map[x] = cnt--;
    for (int i = 1; i <= n; i++) cout << map[i] << ' ';
}