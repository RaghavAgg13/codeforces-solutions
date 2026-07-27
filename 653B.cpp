#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

int n,m;
string a,b;
unordered_map<char, vector<string>> adj;


int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    adj.clear();

    while (m--) {
        cin >> a >> b;
        adj[b[0]].push_back(a);
    }

    queue<string> q;
    q.push("a");
    int cnt = 0;

    while (!q.empty()) {
        auto x = q.front(); q.pop();
        
        if (x.size() == n) {
            cnt++;
            continue;
        }

        char key = x[0];
        
        for (string& nw : adj[key]) {
            string x_next = nw + x.substr(1);
            q.push(x_next);
        }
    }

    cout << cnt << '\n';
}