#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
char mov[] = {'R', 'L', 'D', 'U'};

int n,m,a,b;
vector<string> s;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    pair<int, int> S, init;

    for (int i = 0; i < n; i++) {
        string st;
        cin >> st;
        s.push_back(st);

        for (int j = 0; j < m; j++) {
            if (st[j] == 'S') {
                S = {i,j};
            }
        }
    }
    init = {S.first, S.second};
    
    int moved = 1;
    while (moved) {
        moved = 0;
        for (int i = 0; i < 4; i++) {
            int nx = S.first+dx[i], ny = S.second+dy[i];
    
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            if (s[nx][ny] != '*') continue;
            cout << mov[i];
     
            s[nx][ny] = '.';
            S = {nx, ny};
            moved = 1;
            break;
        }
    }

    for (int i = 0; i < 4; i++) {
        int nx = S.first+dx[i], ny = S.second+dy[i];

        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

        if (init.first == nx && init.second == ny) {
            cout << mov[i];
            return 0;
        }
    }
}