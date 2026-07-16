#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int n,a,s;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    while (n--) {
        cin >> a;

        queue<pair<int, int>> q; q.push({0, a});
        
        bool ans = true;
        while (ans) {
            s = q.size();
            while (s--) {
                auto [d,x] = q.front(); q.pop();
    
                if (!x) {
                    cout << d << ' ';
                    ans = false;
                    break;
                }
    
                q.push({d+1, (x+1)%32768});
                if (x%2 == 0) q.push({d+1, (2*x)%32768});
            }
        }
    }
    
}