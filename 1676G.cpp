#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
string s;
vector<vector<int>> adj;

pair<int, int> recur(int root) {
    pair<int, int> bw = {0,0};
    if (s[root] == 'B') bw.first++;
    else bw.second++;

    for (auto x : adj[root]) {
        pair<int, int> r = recur(x);
        bw.first += r.first; bw.second += r.second;
    }

    if (bw.first == bw.second) b++;

    return bw;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n+1, vector<int>());
        
        for (int i = 2; i <= n; i++) {
            cin >> a;
            adj[a].push_back(i);
        }

        cin >> s; s = " "+s;

        b = 0;
        recur(1);

        cout << b << '\n';
    }
}