#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int t,n,m,a,b;
vector<string> s;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    s.assign(2, "");
    while (t--) {
        cin >> n;
        cin >> s[0];
        cin >> s[1];

        queue<pair<int, int>> q;
        q.push({0,0});

        bool found = false;
        vector<vector<int>> vis(2, vector<int>(n, 0));
        
        while (!q.empty()) {
            auto [x,y] = q.front(); q.pop();

            if (x == 1 && y == n-1) {
                found = true;
                break;
            }

            if (vis[x][y]) continue; vis[x][y] = 1;

            for (int i = 0; i < 4; i++) {
                int nx = x+dx[i], ny = y+dy[i];
                if (nx < 0 || nx >= 2 || ny < 0 || ny >= n) continue;
                if (s[nx][ny] == '>') ny++;
                else ny--;
                if (ny < 0 || ny >= n || ny == y) continue;
                if (vis[nx][ny]) continue;

                q.push({nx, ny});
            }
        }

        if (found) cout << "YES\n";
        else cout << "NO\n";
    }
    
}