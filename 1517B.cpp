#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int t,n,m,a,b;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> m;

        // val, pos
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        vector<vector<int>> arr(n, vector<int>(m)), ans(n, vector<int>(m, -1));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> arr[i][j];
                pq.push({arr[i][j], i, j});
            }
        }

        vector<vector<bool>> used(n, vector<bool>(m, false));

        for (int i = 0; i < m; i++) {
            auto ar = pq.top(); pq.pop();
            int x = ar[0], y = ar[1], z = ar[2];

            ans[y][i] = x;
            used[y][z] = true;
        }

        for (int i = 0; i < n; i++) {
            int ptr = 0;
            for (int j = 0; j < m; j++) {
                if (ans[i][j] == -1) {
                    while (used[i][ptr]) ptr++;
                    ans[i][j] = arr[i][ptr];
                    used[i][ptr] = true;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cout << ans[i][j] << ' ';
            }
            cout << '\n';
        }
    }
}