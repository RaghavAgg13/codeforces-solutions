#include <bits/stdc++.h>
using namespace std;
#define ll long long

vector<int> getSlidingWindowGCD(int n, int k, const vector<int>& arr) {
    vector<int> result;
    if (n < k || k <= 0) return result;
    
    result.reserve(n - k + 1);

    vector<pair<int, int>> stack_in;
    vector<pair<int, int>> stack_out;

    auto push = [&](int val) {
        int current_gcd = val;
        if (!stack_in.empty()) {
            current_gcd = gcd(current_gcd, stack_in.back().second);
        }
        stack_in.push_back({val, current_gcd});
    };

    auto pop = [&]() {
        if (stack_out.empty()) {
            while (!stack_in.empty()) {
                int val = stack_in.back().first;
                stack_in.pop_back();
                
                int current_gcd = val;
                if (!stack_out.empty()) {
                    current_gcd = gcd(current_gcd, stack_out.back().second);
                }
                stack_out.push_back({val, current_gcd});
            }
        }
        stack_out.pop_back();
    };

    auto query = [&]() -> int {
        if (stack_in.empty()) return stack_out.back().second;
        if (stack_out.empty()) return stack_in.back().second;
        return gcd(stack_in.back().second, stack_out.back().second);
    };

    for (int i = 0; i < k; ++i) push(arr[i]);
    result.push_back(query());

    for (int i = k; i < n; ++i) {
        pop();
        push(arr[i]);
        result.push_back(query());
    }

    return result;
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int t, n;
    cin >> t;

    while (t--) {
        cin >> n;
        vector<int> a(n);
        for (auto &it : a) cin >> it;

        vector<int> a_circular = a;
        a_circular.insert(a_circular.end(), a.begin(), a.end());

        int l = 1, r = n;
        int ans = n;
        
        while (l <= r) {
            int mid = l + (r-l)/2;

            vector<int> gcd = getSlidingWindowGCD(2*n, mid, a_circular);
            bool check = true;
            
            if (!gcd.empty()) {
                for (size_t i = 1; i < n; i++) {
                    if (gcd[i] != gcd[i-1]) {
                        check = false;
                        break;
                    }
                }
            }

            if (check) {
                ans = mid;
                r = mid-1;
            } else l = mid+1;
        }

        cout << ans-1 << endl;
    }
}