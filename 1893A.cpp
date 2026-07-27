#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,k,a;
vector<int> idx;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> k;
        vector<int> b(n+1);
        for (int i = 1; i <= n; i++) cin >> b[i];

        idx.assign(n+1, 0);
        for (int i = 1; i <= n; i++) {
            if (b[i] > n) idx[i] = -1;
            else idx[i] = ((i-b[i]-1)%n+n)%n + 1;
        }

        vector<int> vis(n+1, 0);
        int cur = n;

        k = min(n, k);
        while (k > 0 && cur != -1 && !vis[cur]) {
            vis[cur] = 1;
            cur = idx[cur];
            k--;
        }

        if (cur != -1) cout << "YES\n";
        else cout << "NO\n";
    }
}