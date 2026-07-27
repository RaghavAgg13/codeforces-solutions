#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int x,n,k,a,b;
string s,t;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> x;
    while (x--) {
        cin >> n >> k;
        cin >> s;
        cin >> t;

        bool valid = true;
        int freq[26] = {0};
        for (int i = 0; i < n; i++) {
            freq[s[i]-'a']++;
            freq[t[i]-'a']--;
        }

        for (int i = 0; i < 26; i++) {
            if (freq[i] != 0) {
                valid = false;
                break;
            }
        }

        if (n == 5) {
            if (s[2] != t[2]) valid = false;
        }
        else if (n == 4) {
            if (s[1] != t[1] || s[2] != t[2]) valid = false;
        }
        else if (n <= 3 && s != t) valid = false;

        if (valid) cout << "YES\n";
        else cout << "NO\n";
    }   
}