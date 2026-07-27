#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int t,n,m,a,b;
string s;
vector<int> lft,rht;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> s;
        n = s.size();
        
        bool pos = true;
        lft.assign(26, -1); rht.assign(26, -1);
        for (int i = 0; i < n; i++) s[i] -= 'a';
        
        int cur = s[0];
        for (int i = 1; i < n; i++) {
            int nxt = s[i];

            if (lft[cur] == nxt || rht[cur] == nxt) {
                cur = nxt;
            }
            else if (lft[cur] == -1 && lft[nxt] == -1 && rht[nxt] == -1) {
                lft[cur] = nxt;
                rht[nxt] = cur;
                cur = nxt;
            }
            else if (rht[cur] == -1 && lft[nxt] == -1 && rht[nxt] == -1) {
                rht[cur] = nxt;
                lft[nxt] = cur;
                cur = nxt;
            }
            else {
                pos = false;
                break;
            }
        }

        if (!pos) {
            cout << "NO\n";
            continue;
        }

        cout << "YES\n";
        int freq[26] = {0};

        int l = s[0];
        while (lft[l] != -1) {
            l = lft[l];
        }

        string f = "";
        while (l != -1) {
            f += (char)(l+'a');
            freq[l]++;
            l = rht[l];
        }

        cout << f;
        for (int i = 0; i < 26; i++) {
            if (!freq[i]) cout << (char)(i+'a');
        }
        cout << '\n';
    }
}