balance = int(input())
print(balance//100 + (balance%100)//20 + ((balance%100)%20)//10 + (((balance%100)%20)%10)//5 + (((((balance%100)%20)%10)%5)//1))