#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int t,n;
string s;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> s;
        s = "R"+s+"R";
        n = s.length();

        int prev = 0, len = 0;
        for (int i = 1; i < n; i++) {
            if (s[i] == 'R') {
                len = max(len, i-prev);
                prev = i;
            }
        }

        cout << len << '\n';
    }
}