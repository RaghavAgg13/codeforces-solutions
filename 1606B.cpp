#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
 
ll t,n,k;
 
int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n>>k;
        
        ll patched = 1;
        ll time = 0;

        while (patched < min(n,k)) {
            time++;
            patched += min(k, patched);
        }

        if (patched >= n) {
            cout << time << endl;
        } else {
            time += (n-patched)/k+((n-patched)%k>0);
            cout << time << endl;
        }
        
    }  
}