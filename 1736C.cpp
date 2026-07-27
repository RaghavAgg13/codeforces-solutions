#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
string s;
vector<int> map, used;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        cin >> s;
        map.assign(26, -1);
        used.assign(26, 0);

        for (int i = 0; i < n; i++) {
            if (map[s[i]-'a'] == -1) {
                for (int j = 0; j < 26; j++) {
                    if (used[j]) continue;

                    // check for any incorrect <26 length cycles
                    map[s[i]-'a'] = j;
                    int length = 0, base = s[i]-'a', cur = s[i]-'a';
                    while (map[cur] != -1) {
                        cur = map[cur];
                        length++;
                        if (cur == base) {
                            cur = 99;
                            break;
                        }
                    }

                    if (cur == 99 && length < 26) {
                        map[s[i]-'a'] = -1;
                    }
                    else {
                        used[j] = 1;
                        break;
                    };
                }
            }

            cout << (char)(map[s[i]-'a']+'a');
        }
        cout << '\n';
    }
}