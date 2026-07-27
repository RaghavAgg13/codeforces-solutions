#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        
        for (int i = 1; i <= n; i++) {
            for (int j = i+1; j <= n; j++) {
                if ((j-i)*2 < n) cout << "1 ";
                else if ((j-i)*2 == n) cout << "0 ";
                else cout << "-1 ";
            }
        }
        
        cout << '\n';
    }
}