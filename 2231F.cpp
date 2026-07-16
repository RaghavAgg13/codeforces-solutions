#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
using namespace std;

int t,n,m,a,b;
vector<int> vis;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> m;
        vis.assign(n+1, 0);
        int query_id = 0;

        while (m--) {
            cin >> a >> b;
            
            query_id++;
            int ans = 0;
            
            int sq = sqrt(abs(a-b));
            if (sq*sq == abs(a-b)) {
                cout << "1\n";
                continue;
            }
        
            // chk for d=2
            for (int i = 1; i*i <= n; i++) {
                if (a+i*i <= n) {
                    int sq = sqrt(abs(a+i*i-b));
                    if (sq*sq == abs(a+i*i-b)) {
                        ans = 2;
                        break;
                    }
                }
                if (a-i*i > 0) {
                    int sq = sqrt(abs(a-i*i-b));
                    if (sq*sq == abs(a-i*i-b)) {
                        ans = 2;
                        break;
                    }
                }
            }

            if (ans == 2) {
                cout << "2\n";
                continue;
            }
            
            // chk for d=3
            vector<int> na;
            for (int i = 1; i*i <= n; i++) {
                if (a+i*i <= n) na.push_back(a+i*i);
                if (a-i*i > 0) na.push_back(a-i*i);
            }
            for (int i = 1; i*i <= n; i++) {
                if (b+i*i <= n) vis[b+i*i] = query_id;
                if (b-i*i > 0) vis[b-i*i] = query_id;
            }

            for (auto x : na) {
                for (int i = 1; i*i <= n; i++) {
                    if (x+i*i <= n && vis[x+i*i] == query_id) { 
                        ans = 3;
                        break;
                    }
                    if (x-i*i > 0 && vis[x-i*i] == query_id) {
                        ans = 3;
                        break;
                    }
                }
                if (ans == 3) break;
            }

            if (ans == 3) cout << "3\n";
            else cout << "4\n";
        }
    }
}