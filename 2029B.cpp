#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
#define ll long long

int t,n,m,n1,n2;
string s,r;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        cin >> s;
        cin >> r;
        
        n1 = 0, n2 = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') n1++;
            else n2++;
        }

        bool chk = true;
        for (int i = 0; i < n-1; i++) {
            if (n1 == 0 || n2 == 0) {
                chk = false;
                break;
            }
            if (r[i] == '1') n2--;
            else n1--;
        }
        
        if (chk) cout << "YES\n";
        else cout << "NO\n";
    }
}