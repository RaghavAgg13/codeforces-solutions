for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    a.sort(reverse=True)
 
    final_numbers = set()

    for i in a:
        if i+1 not in final_numbers:
            final_numbers.add(i+1)
        else:
            final_numbers.add(i)
    
    print(len(final_numbers))