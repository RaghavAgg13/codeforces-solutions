#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int t,n,m;
string a;
vector<vector<int>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n, vector<int>());

        for (int i = 0; i < n; i++) {
            cin >> a;
            for (int j = 0; j < n; j++) {
                if (a[j] == '1') {
                    adj[j].push_back(i);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            cout << adj[i].size() << ' ';
            for (auto x : adj[i]) cout << x+1 << ' ';
            cout << '\n';
        }
    }
}