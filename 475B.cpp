#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int n,m,a,b;
string hor,ver;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    cin >> hor;
    cin >> ver;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int cnt = 1;
            vector<int> vis(n*m, 0); 
            vis[i*m+j] = 1;

            queue<pair<int, int>> q;
            q.push({i, j});

            while (!q.empty()) {
                auto [x,y] = q.front(); q.pop();
                
                for (int i = 0; i < 4; i++) {
                    int nx = x+dx[i], ny = y+dy[i];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                    if (i < 2) {
                        if (i == 0 && hor[x] == '<') continue;
                        else if (i == 1 && hor[x] == '>') continue;
                    } else {
                        if (i == 2 && ver[y] == '^') continue;
                        else if (i == 3 && ver[y] == 'v') continue;
                    }
                    
                    if (vis[nx*m+ny]) continue; vis[nx*m+ny] = 1;
                    cnt++;
                    q.push({nx, ny});
                }

            }
            if (cnt != n*m) {
                cout << "NO";
                return 0;
            }
        }
    }
    cout << "YES";
}