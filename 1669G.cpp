#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
string s;
vector<vector<int>> grid;
vector<pair<int, int>> obs;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> m;
        grid.assign(n, vector<int>(m, 1));
        obs.clear();

        for (int i = 0; i < n; i++) {
            cin >> s;
            for (int j = 0; j < m; j++) {
                if (s[j] == '.') grid[i][j] = 0;
                else if (s[j] == 'o') grid[i][j] = -1;
                else obs.push_back({i,j});
            }
        }

        reverse(obs.begin(), obs.end());

        while (obs.size() > 0) {
            vector<pair<int, int>> new_obs;
            for (auto [x,y] : obs) {
                int nx = x+1, ny = y;
                if (nx >= n) continue;
                if (grid[nx][ny] != 0) continue;
    
                grid[x][y] = 0;
                grid[nx][ny] = 1;
                new_obs.push_back({nx,ny});
            }

            obs = new_obs;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == -1) cout << 'o';
                else if (!grid[i][j]) cout << '.';
                else cout << "*";
            }
            cout << '\n';
        }
    }
    
}