#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n;
    cin >> n;

    while (n--) {
        int t;
        cin >> t;

        if (t >=6) cout << t%2 << '\n';
        else {
            if (t <= 3) cout << t << '\n';
            else cout << "0\n";
        }
    }
}

