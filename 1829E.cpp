#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int t,n,m,a,b;
vector<vector<int>> grid, vis;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> m;
        grid.assign(n, vector<int>(m));
        vis.assign(n, vector<int>(m, 0));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) cin >> grid[i][j];
        }
        
        int ans = 0;
        queue<pair<int, int>> q;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (vis[i][j] || !grid[i][j]) continue;
                int sum = 0;

                q.push({i,j});
                while (!q.empty()) {
                    auto [x,y] = q.front(); q.pop();

                    if (vis[x][y]) continue; vis[x][y] = 1;
                    sum += grid[x][y];

                    for (int k = 0; k < 4; k++) {
                        int nx = x+dx[k], ny = y+dy[k];
                        if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                        if (vis[nx][ny] || !grid[nx][ny]) continue;

                        q.push({nx, ny});
                    }
                }

                ans = max(ans, sum);
            }
        }
        
        cout << ans << '\n';
    }
}