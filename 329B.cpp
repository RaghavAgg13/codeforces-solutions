#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int n,m,a,b;
pair<int, int> s,t;
vector<string> grid;
vector<int> vis;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    grid.resize(n);

    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'S') s = {i,j};
            else if (grid[i][j] == 'E') t = {i,j};
        }
    }

    b = 1e9;
    vis.assign(n*m, 0);
    vis[s.first*m + s.second] = 1;

    queue<vector<int>> q;
    q.push({0, s.first, s.second});

    while (!q.empty()) {
        auto arr = q.front(); q.pop();
        int x = arr[1], y = arr[2], dist = arr[0];
        
        if (dist > b) continue;
        if (grid[x][y] == 'E') b = dist;

        for (int i = 0; i < 4; i++) {
            int nx = x+dx[i], ny = y+dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (vis[nx*m + ny] || grid[nx][ny] == 'T') continue;
            vis[nx*m + ny] = 1;

            q.push({dist+1, nx, ny});
        }
    }

    a = 0;
    q.push({t.first, t.second, 0});

    vis[t.first*m + t.second] = 2;

    while(!q.empty()) {
        auto arr = q.front(); q.pop();
        int x = arr[0], y = arr[1], dist = arr[2];
        if (dist > b) continue;

        if ('1' <= grid[x][y] && grid[x][y] <= '9') a += grid[x][y]-'1'+1;

        for (int i = 0; i < 4; i++) {
            int nx = x+dx[i], ny = y+dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (vis[nx*m + ny] == 2 || grid[nx][ny] == 'T') continue;
            vis[nx*m + ny] = 2;

            q.push({nx, ny, dist+1});
        }
    }

    cout << a;
}