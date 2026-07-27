#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,x1,y_1,x2,y2;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> x1 >> y_1 >> x2 >> y2;
    vector<vector<int>> dist_map(n+1, vector<int>(n+1, 1e9));

    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    pq.push({0, x1, y_1});
    dist_map[x1][y_1] = 0;

    while (!pq.empty()) {
        auto arr = pq.top(); pq.pop();
        auto dist = arr[0], x = arr[1], y = arr[2];

        if (dist > dist_map[x][y]) continue;
        if (x == x2 && y == y2) {
            cout << dist;
            return 0;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x+dx[i], ny = y+dy[i];

            if (((nx == 0 || nx == n) && 0 <= ny && ny <= n) ||
                ((ny == 0 || ny == n) && 0 <= nx && nx <= n)) {
                if (dist+1 >= dist_map[nx][ny]) continue;

                dist_map[nx][ny] = dist+1;
                pq.push({dist+1, nx, ny});
            }
        }
    }
}