#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int t,n,a,b,c;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> a >> b >> c;

        if (!a && !c) {
            cout << "1";
        }

        if (a && c) b--;

        char s = (c == 0 && a > 0) ? '1' : '0';

        if (a) a++;
        if (c) c++;
        
        while (a--) cout << "0";
        while (c--) cout << "1";
        
        while (b-- > 0) {
            cout << s;

            if (s == '0') s = '1';
            else s = '0';
        }
        cout << '\n';
    }
    
}