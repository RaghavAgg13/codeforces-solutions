#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
int wt[] = {4, 1, 2, 8};

int n,m,a,b;
vector<vector<int>> grid,vis;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    grid.assign(n, vector<int>(m));
    vis.assign(n, vector<int>(m, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cin >> grid[i][j];
    }

    queue<pair<int, int>> q;
    vector<int> rooms;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (vis[i][j]) continue; vis[i][j] = 1;
            q.push({i,j});

            b = 0;
            while (!q.empty()) {
                auto [x,y] = q.front(); q.pop();
                b++;

                for (int i = 0; i < 4; i++) {
                    if (grid[x][y]&wt[i]) continue;
                    int nx = x+dx[i], ny = y+dy[i];
                    if (vis[nx][ny]) continue; vis[nx][ny] = 1;

                    q.push({nx, ny});
                }
            }

            rooms.push_back(b);
        }
    }
    sort(rooms.begin(), rooms.end(), greater<int>());
    for (auto &x : rooms) cout << x << ' ';
}