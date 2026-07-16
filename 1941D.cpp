#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int t,n,m,x,a;
string b;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> m >> x;
        
        set<int> q,qs;
        q.insert(x-1);

        while (m--) {
            cin >> a >> b; a = a%n;

            qs.clear();
            for (auto x : q) {
                if (b == "0") qs.insert((x+a)%n);
                else if (b == "1") qs.insert((x-a+n)%n);
                else {
                    qs.insert((x+a)%n);
                    qs.insert((x-a+n)%n);
                }
            }
            q = qs;
        }

        cout << q.size() << '\n';
        for (auto x : q) cout << x+1 << ' ';
        cout << '\n';
    }
    
}