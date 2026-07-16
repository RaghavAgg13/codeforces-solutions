#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> n >> m;
    vector<int> ans = {m};

    while (m > n) {
        if (m%10 == 1) {
            ans.push_back(m/10);
            m /= 10;
        }
        else if (m%2 == 0) {
            ans.push_back(m/2);
            m /= 2;
        }
        else break;
    }

    if (m != n) cout << "NO\n";
    else {
        cout << "YES\n";

        reverse(ans.begin(), ans.end());
        cout << ans.size() << '\n';
        for (auto x : ans) cout << x << ' ';
    }
    
}