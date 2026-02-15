for i in range(int(input())):
    s = input()
    try:
        n1,n2 = s.split("C")
        n1, n2 = int(n1[1:]), int(n2)

        letters = []

        while n2 > 26:
            n2 -= 1
            letters.append(chr(n2%26+65))
            n2 //= 26
        letters += chr(n2+64)

        print(''.join(reversed(letters)), n1, sep='') 

    except ValueError:
        letters = []
        numbers = []

        for ch in s:
            (letters if ch.isalpha() else numbers).append(ch)

        letters = letters[::-1]
        n = 0
        for i in range(len(letters)):
            n += (ord(letters[i])-64)*(26**(i))
        
        print("R",''.join(numbers),"C",n, sep='')    