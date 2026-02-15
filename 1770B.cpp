#include <iostream>
#include <vector>
using namespace std;
#define ll long long
 
int t,n,k;
 
int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n>>k;
        
        if (k == 1) {
            for (int i = 1; i < n+1; i++) cout << i << ' ';
            cout << endl;
            continue;
        }

        vector<int> arr(n);
        int l = 1, r = n;
        for (int i = 0; i < n; i += (k-1)*2) {
            for (int j = i; j < min(n, i+k-1); j++) {
                arr[j] = r--;
            }
            for (int j = i+k-1; j < min(n, i+k*2-2); j++) {
                arr[j] = l++;
            }
        }
        
        for (int i = 0; i < n; i++) cout << arr[i] << ' ';
        cout << endl;
    }    
}