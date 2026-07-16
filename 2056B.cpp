#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int t,n,m,a,b;
string str;
vector<vector<int>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n+1, vector<int>());
        vector<int> in(n+1, 0);

        for (int i = 1; i <= n; i++) {
            cin >> str; str = " "+str;
            
            for (int j = i+1; j <= n; j++) {
                if (str[j] == '1') {
                    adj[i].push_back(j);
                    in[j]++;
                }
                else {
                    adj[j].push_back(i);
                    in[i]++;
                }
            }
        }

        queue<int> s;
        vector<int> topo;
        for (int i = 1; i <= n; i++) {
            if (!in[i]) s.push(i);
        }

        while (!s.empty()) {
            auto x = s.front(); s.pop();
            topo.push_back(x);

            for (auto y : adj[x]) {
                if (--in[y] == 0) s.push(y);
            }
        }

        for (auto x : topo) cout << x << ' ';
        cout << '\n';
    }
    
}