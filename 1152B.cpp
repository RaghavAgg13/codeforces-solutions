#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int x,m,a,b;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> x;
    vector<int> pts;
    int ops = 0;

    while (x&(x+1)) {
        if (ops%2) x++;
        else {
            int msb = 0;
            for (int i = 29; i >= 0; i--) {
                if ((x>>i)&1) {
                    msb = i;
                    break;
                }
            }

            int n_val = 0;
            for (int i = msb; i >= 0; i--) {
                if (((x>>i)&1) == 0) {
                    n_val = i+1;
                    break;
                }
            }

            pts.push_back(n_val);
            x ^= (1<<n_val)-1;
        }
        ops++;
    }

    cout << ops << '\n';
    for (auto x : pts) cout << x << ' ';
    
}