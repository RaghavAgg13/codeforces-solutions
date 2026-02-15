#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int n;
    cin >> n;

    string x = "", y = "";
    map<string, int> b;
    for (int i = 0; i < n; i++) {
        string a;
        cin >> a;

        b[a]++;
        
        if (x == "") x = a;
        else if (x != a && y == "") y = a;

    }
    if (b[x] > b[y]) cout << x << endl;
    else cout << y << endl;
}