#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int n,m,r1,c1,r2,c2;
string s;
vector<string> grid;
vector<vector<int>> vis;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    cin >> r1 >> c1;
    cin >> r2 >> c2;
    r1--; c1--; r2--; c2--;
    grid.resize(n);
    vis.assign(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) cin >> grid[i];

    int sec = 0, sec1 = -1, sec2 = -1;
    vector<vector<int>> sections;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (vis[i][j] || grid[i][j] == '1') continue; vis[i][j] = 1;
            sections.push_back({i*n+j});

            queue<pair<int, int>> q;
            q.push({i,j});

            while (!q.empty()) {
                auto [x,y] = q.front(); q.pop();
                if (x == r1 && y == c1) sec1 = sec;
                if (x == r2 && y == c2) sec2 = sec;

                for (int i = 0; i < 4; i++) {
                    int nx = x+dx[i], ny = y+dy[i];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    if (vis[nx][ny] || grid[nx][ny] == '1') continue;
                    vis[nx][ny] = 1;

                    sections[sec].push_back(nx*n+ny);
                    q.push({nx, ny});
                }
            }
            sec++;
        }
    }

    if (sec1 == sec2) cout << "0";
    else {
        int ans = (int)1e9;
        for (auto p1 : sections[sec1]) {
            for (auto p2 : sections[sec2]) {
                ans = min(ans, (p1/n-p2/n)*(p1/n-p2/n)+(p1%n-p2%n)*(p1%n-p2%n));
            }
        }
        cout << ans;
    }
}