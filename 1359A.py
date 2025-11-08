for i in range(int(input())):
    n,m,k = list(map(int, input().split()))

    cards_per_person = n//k
    if cards_per_person >= m: print(f"{m}")
    else:
        other = (m-cards_per_person)//(k-1)+bool((m-cards_per_person)%(k-1))

        if (other == cards_per_person) or (other > 1 and other-1 == cards_per_person): print(0)
        else: print(cards_per_person-other)