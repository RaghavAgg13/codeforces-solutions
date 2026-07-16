#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<int> arr;
vector<vector<int>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> m;
        arr.assign(n+1, 0);
        adj.assign(n+1, vector<int>());

        while (m--) {
            cin >> a >> b;
            arr[a]++; arr[b]++;

            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        a = 0;
        for (int i = 1; i <= n; i++) {
            if (adj[i].size() == 1) {
                arr[i]--;
                arr[adj[i][0]]--;
                a++;
            }
        }

        b = 0;
        for (int i = 1; i <= n; i++) {
            if (arr[i] == 1) b++;
        }

        cout << b << " " << a/b << '\n';
    }
    
}