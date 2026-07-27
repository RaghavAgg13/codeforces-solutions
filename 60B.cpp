#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int dx[] = {0,0,0,0,1,-1};
int dy[] = {0,0,1,-1,0,0};
int dz[] = {1,-1,0,0,0,0};

int h,n,m,a,b;
vector<vector<string>> grid;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> h >> n >> m;
    grid.assign(h, vector<string>(n));
    
    for (int k = 0; k < h; k++) {
        for (int i = 0; i < n; i++) {
            cin >> grid[k][i];
        }
    }

    cin >> a >> b;
    a--; b--;

    queue<vector<int>> q; q.push({a,b,0});
    grid[0][a][b] = '#'; 
    b = 1;
    
    while (!q.empty()) {
        auto arr = q.front(); q.pop();
        auto x = arr[0], y = arr[1], z = arr[2];
        
        for (int i = 0; i < 6; i++) {
            auto nx = x+dx[i], ny = y+dy[i], nz = z+dz[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || nz < 0 || nz >= h || grid[nz][nx][ny] == '#') continue;
            grid[nz][nx][ny] = '#';
            b++;
            
            q.push({nx, ny, nz});
        }
    }

    cout << b;
}