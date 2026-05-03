#include <iostream>
#include <queue>
using namespace std;
 
int t,n,m;
 
int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n>>m;
        queue<int> Q;
        Q.push(n);

        int found = (n==m);
        while (!Q.empty()) {
            int no = Q.front();
            Q.pop();

            if (no%3) break;
            int n1 = no/3, n2 = 2*(no/3);

            if (n1 == m || n2 == m) {
                found = 1;
                break;
            }

            if (n1 > m) Q.push(n1);
            if (n2 > m) Q.push(n2);
        }
        
        if (found) cout << "Yes\n";
        else cout << "No\n";
    }    
}