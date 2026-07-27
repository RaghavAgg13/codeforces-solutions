#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int n,d;
string a;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> d;
    cin >> a;

    priority_queue<pair<int, int>, vector<pair<int, int>>> pq;
    pq.push({0, 0});

    while (!pq.empty()) {
        auto [x, jumps] = pq.top(); pq.pop();

        if (x == n-1) {
            cout << jumps;
            return 0;
        }

        pq = priority_queue<pair<int, int>, vector<pair<int, int>>>();
        for (int i = min(n-x, d); i >= 1; i--) {
            if (a[x+i] == '1') {
                pq.push({x+i, jumps+1});
                break;
            }
        }
    }

    cout << -1;
}