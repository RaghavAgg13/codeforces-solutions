#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int n,m,a,b;
vector<string> grid;
vector<vector<int>> vis;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    grid.resize(n);
    vis.assign(n, vector<int>(m, 0));

    for (int i = 0; i < n; i++) cin >> grid[i];

    queue<pair<int, int>> q;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (vis[i][j]) continue; vis[i][j] = 1;
            q.push({i*m+j, -1});

            while (!q.empty()) {
                auto [pt, par] = q.front(); q.pop();
                int x = pt/m, y = pt%m;

                for (int i = 0; i < 4; i++) {
                    int nx = x+dx[i], ny = y+dy[i];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                    if (grid[x][y] != grid[nx][ny]) continue;

                   if (vis[nx][ny]) {
                        if (nx*m+ny != par) {
                            cout << "Yes";
                            return 0;
                        }
                        continue;
                    }

                    vis[nx][ny] = 1;
                    q.push({nx*m+ny, pt});
                }
            }
        }
    }

    cout << "No";
}