#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

int t,n,m,a,b;
string s;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        cin >> s;
    
        b = n-1;
        for (int i = 0; i < n-2; i++) {
            if (s[i] == s[i+2]) b--;
        }
    
        cout << b << '\n';
    }
}