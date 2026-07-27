#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
char from[] = {'L', 'R', 'U', 'D'};

int t,n,m,a,b;
string s;
vector<string> grid;
vector<vector<int>> escaped;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
 
    cin >> t;
    while (t--) {
        cin >> n >> m;
        grid.resize(n);
        for (int i = 0; i < n; i++) cin >> grid[i];
        
        escaped.assign(n, vector<int>(m, 0));
        
        queue<pair<int, int>> q;
        for (int i = 0; i < n; i++) {
            if (grid[i][0] == 'L') {
                q.push({i,0});
                escaped[i][0] = 1;
            }
            if (grid[i][m-1] == 'R') {
                q.push({i,m-1});
                escaped[i][m-1] = 1;
            }
        }
        for (int j = 0; j < m; j++) {
            if (grid[0][j] == 'U') {
                q.push({0,j});
                escaped[0][j] = 1;
            }
            if (grid[n-1][j] == 'D') {
                q.push({n-1,j});
                escaped[n-1][j] = 1;
            }
        }
        int esc = q.size();

        while (!q.empty()) {
            auto [x,y] = q.front(); q.pop();

            for (int i = 0; i < 4; i++) {
                int nx = x+dx[i], ny = y+dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (escaped[nx][ny] || grid[nx][ny] == '?') continue;
                if (grid[nx][ny] != from[i]) continue;

                escaped[nx][ny] = 1;
                esc++;
                q.push({nx, ny});
            }
        }

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (grid[x][y] == '?') {
                    int esc_cnt = 0, ag = 0;

                    for (int i = 0; i < 4; i++) {
                        int nx = x+dx[i], ny = y+dy[i];
                        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                        ag++;

                        if (escaped[nx][ny]) esc_cnt++;
                    }

                    if (esc_cnt == ag) {
                        esc++;
                        escaped[x][y] = 1;
                    }
                }
            }
        }

        cout << n*m-esc << '\n';
    }
}