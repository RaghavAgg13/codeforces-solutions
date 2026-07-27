#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int n,m,k,a,b;
vector<string> grid;
vector<vector<int>> map;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;
    grid.resize(n);
    map.assign(n, vector<int>(m, 0));

    for (int i = 0; i < n; i++) cin >> grid[i];
    
    queue<pair<int, int>> q;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] != '.') continue;
            int cnt = 0;
            
            vector<int> grp = {i*m+j};
            q.push({i,j});
            grid[i][j] = '0';
            
            while (!q.empty()) {
                auto [x,y] = q.front(); q.pop();

                for (int i = 0; i < 4; i++) {
                    int nx = x+dx[i], ny = y+dy[i];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                    
                    if (grid[nx][ny] == '*') cnt++;
                    else if (grid[nx][ny] == '.'){
                        grp.push_back(nx*m+ny);
                        grid[nx][ny] = '0'; 
                        q.push({nx, ny});
                    }
                }
            }
            
            for (auto pt : grp) {
                a = pt/m, b = pt%m;
                map[a][b] = cnt;
            }
        }
    }

    while (k--) {
        int ans = 0;
        cin >> a >> b;

        cout << map[a-1][b-1] << '\n';
        continue;
    }
}