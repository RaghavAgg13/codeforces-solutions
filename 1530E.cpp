#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        string s;
        cin >> s;
        sort(s.begin(), s.end());

        char stack[s.length()];
        int top = 0;

        for (int i = 0; i < s.length(); i++) {
            if (top) {
                cout << stack[--top];
                stack[top++] = s[i];
            }
            else if (s[i] != s[i+1]) {
                cout << s[i];
            }
            else {
                stack[top++] = s[i];
            }
        }
        while (top) cout << stack[--top];
        cout << endl;
    }
}