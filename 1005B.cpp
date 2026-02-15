#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    string a, b;
    cin >> a >> b;

    int top = a.length();
    int ptr = b.length();

    while (top && ptr && a[top-1] == b[ptr-1]) {
        top--; ptr--;
    }
    cout << top+ptr << endl;
}