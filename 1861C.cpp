#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int t,n,m,a,b;
string s;
vector<int> arr;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> s;
        n = s.size();
        
        arr.assign(n+1, 0);
        b = 0;
        bool pos = true;
        
        // arr[i] = 0 means unset, = 1 means set pos, -1 means set neg
        for (int i = 0; i < n; i++) {
            if (s[i] == '+') {
                b++;
                if (b == 1) arr[b] = 1;
                else if (arr[b-1] == -1) arr[b] = -1;
                else arr[b] = 0;
            }
            else if (s[i] == '-') {
                b--;
            }
            else if (s[i] == '1') {
                if (b <= 1) continue;

                for (int j = b; j >= 1; j--) {
                    if (arr[j] == 1) break;
                    if (arr[j] == -1) {
                        pos = false;
                        break;
                    }
                    arr[j] = 1;
                }
            }
            else {
                if (b < 2 || arr[b] == 1) {
                    pos = false;
                    break;
                }
                arr[b] = -1;    
            }

            if (!pos) break;
        }

        if (pos) cout << "YES\n";
        else cout << "NO\n";
    }
}