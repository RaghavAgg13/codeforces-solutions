from math import lcm
for i in range(int(input())):
    a,b,c,m = list(map(int, input().split()))
    a_,b_,c_ = (m//a), (m//b), (m//c)

    d,e,f = lcm(a,b), lcm(b,c), lcm(a,c)
    d_,e_,f_ = (m//d), (m//e), (m//f)

    g = lcm(a,b,c)
    g_ = (m//g)

    print(  (a_-d_-f_+g_)*6 + (d_-g_)*3 + (f_-g_)*3 + g_*2, (b_-d_-e_+g_)*6 + (d_-g_)*3 + (e_-g_)*3 + g_*2, (c_-e_-f_+g_)*6 + (e_-g_)*3 + (f_-g_)*3 + g_*2 )