def solve():
    n = int(input())
    if n == 0: return
    
    sum_of_second_mins = 0
    min_of_first_mins = float('inf')
    min_of_second_mins = float('inf')

    for _ in range(n):
        input()
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        first_min = arr[0]
        second_min = arr[1]
        
        min_of_first_mins = min(min_of_first_mins, first_min)
        sum_of_second_mins += second_min
        min_of_second_mins = min(min_of_second_mins, second_min)

    if n == 1:
        print(min_of_first_mins)
        return

    max_beauty = sum_of_second_mins - min_of_second_mins + min_of_first_mins
    print(max_beauty)

for i in range(int(input())):
    solve()