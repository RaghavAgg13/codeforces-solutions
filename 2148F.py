for _ in range(int(input())):
    n = int(input())
    elements = []
    for j in range(n):
        a = list(map(int, input().split()))
        
        k = a[0]
        seq = a[1:]
        elements.append(seq)

    final = []
    while elements:
        idx = min(range(len(elements)), key=lambda i: elements[i])
        best_seq = elements[idx]
        final.extend(best_seq)

        l = len(best_seq)
        d = []
        for i in range(len(elements)):
            if i == idx:
                continue
            
            seq = elements[i]
            if len(seq) > l: d.append(seq[l:])
        
        elements = d

    print(*final)