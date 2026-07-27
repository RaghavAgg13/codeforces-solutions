#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<vector<int>> adj;

int dfs(int x) {
    int max1 = -1, max2 = -1;

    for (auto y : adj[x]) {
        int h = dfs(y); 

        if (h > max1) {
            max2 = max1;
            max1 = h;
        }
        else if (h > max2) max2 = h;
    }

    if (max2 != -1) b += max2+1;
    return max1+1;
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
        
        b = 0;
        dfs(1);
        cout << n+b << '\n';
    }
}